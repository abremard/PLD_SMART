import React, {Component} from 'react';
import {Link} from 'react-router-dom';

import { database } from 'firebase/firebase';
import Dropzone from 'react-dropzone'
import { saveAs } from 'file-saver';
import ProgressButton from "react-progress-button";
import {toast, Toaster} from "react-hot-toast";

import ResultTile from "./ResultTile";
import FileTile from "./FileTile";

import alternative from "../images/alternative.png"
import disco from "../images/disco.png"
import electronic from "../images/electronic.png"
import hiphop from "../images/hip hop.png"
import indie from "../images/indie.png"
import jazz from "../images/jazz.png"
import rock from "../images/rock.png"

import 'react-image-picker/dist/index.css'
import '../button.css'


const styleList = [alternative, disco, electronic, hiphop, indie, jazz, rock];
const admin = require('firebase-admin');
const serviceAccount = require('../database/firestore/cred.json');


export default class MatchComp extends Component{
    constructor(props) {
        super(props)
        this.state = {
            files: [],
            buttonState: '',
            isLoading: false,
            hasResult:false,
            downloadLink: '',
            fileName: 'New Creation',
        }
        this.onDrop = this.onDrop.bind(this);
        this.generateFile = this.generateFile.bind(this);
    }

    onDrop(acceptedFiles){
        console.log(acceptedFiles);
        var filesTemp = this.state.files;
        acceptedFiles.forEach(item => {
            if (filesTemp.length<10) {
                filesTemp.push(item);
            }
        });

        this.setState(state => {
            return {
                files: filesTemp,
            };
        })
    }

    generateFile() {
        //get files with FileReader API as blobs
        var formData = new FormData();
        var fileindex = 0;  
        this.state.files.map((file) => {
            formData.append(`file${fileindex}`, file);
            fileindex = fileindex +1;
            const reader = new FileReader();
            reader.onabort = () => toast.error("file reading was aborted");
            reader.onerror = () => toast.error('file reading has failed')
            reader.onload = () => {
                // Do whatever you want with the file contents
                //more on https://developer.mozilla.org/en-US/docs/Web/API/FileReader
                const binaryStr = reader.result
                console.log(binaryStr)
            }
            reader.readAsArrayBuffer(file)
        });

        this.setState({
            isLoading: true,
            buttonState: 'loading',
        });

        admin.initializeApp({
            credential: admin.credential.cert(serviceAccount)
          });

        const database = admin.firestore();
        const docRef = database.collection('ids').doc('serverid');
        docRef.get().then((doc) => {
        if (doc.exists) {
            console.log("Document data:", doc.data());
            const dataretrieved = JSON.stringify(doc.data);
            console.log("dataretrieved");
        } else {
            // doc.data() will be undefined in this case
            console.log("No such document!");
        }
        }).catch(function(error) {
            console.log("Error getting document:", error);
        });

        fetch(`http://aa41a02e41fb.ngrok.io/api/v1/compose/monophonic/lstm/v0?length=200&nb_files=${(fileindex)}`, {
            // content-type header should not be specified!
            method: 'POST',
            body: formData,
          })
            .then(response => response.blob())
            .then( blob => saveAs(blob, 'music.mid'))
            .then(success => {this.setState({
                isLoading: false,
                buttonState: 'success',
                hasResult: true,
                downloadLink: '', //insert download link...,
                files: []
            })}).catch((error) => {
                    toast.error("Something went wrong. Please try again later");
                    this.setState({
                        isLoading: false,
                        buttonState: 'error',
                        hasResult: false,
                    });
                })
    }

    render() {
        const selectedStyle = {
            color: 'white',
            backgroundColor: 'black',
            border: 'solid white 1px',
            marginBottom: '20px',
        };
        const generateStyle = {
            padding: '20px',
        };
        return(
            <>
                <div className="toaster"><Toaster/></div>
                <div className="scratch">
                    <Link to="/studio">back to studio</Link>
                    <h4>Perfect Match</h4>
                    <p>Create a completely new musical piece using your own favorite sounds as the inspiration.
                        Upload up to 10 midi files of your choosing - any style, any artist, any instrument. Ilolio
                        will create a brand new midi file inspired by your uploads. Uses the LSTM algorithm.</p>
                    <ResultTile isLoading={this.state.isLoading} downloadLink={this.state.downloadLink} fileName={this.state.fileName} hasResult={this.state.hasResult}></ResultTile>
                    <h5>Upload your files</h5>
                    <div className="files">
                        {this.state.files.map(item => (
                            <FileTile fileName={item.name} downloadLink={""}></FileTile>
                        ))}
                        <Dropzone onDrop={this.onDrop}>
                            {({getRootProps, getInputProps}) => (
                                <section>
                                    <div className="tile" {...getRootProps()}>
                                        <h4>Upload File</h4>
                                        <div className="zone">
                                            <input {...getInputProps()} />
                                            <p>Drag & drop some files here, or click to select files</p>
                                        </div>
                                    </div>
                                </section>
                            )}
                        </Dropzone>
                    </div>
                    <h6><br/> </h6>
                    <ProgressButton onClick={this.generateFile} state={this.state.buttonState}>
                        Generate
                    </ProgressButton>
                    <h5> </h5>
                </div>
            </>
        )

    }
}