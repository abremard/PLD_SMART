import logo from '../images/logowhite.png'
import {Link} from 'react-router-dom';

import React, {Component} from 'react';
import ResultTile from "./ResultTile";
import ImagePicker from "react-image-picker";
import { Multiselect } from 'multiselect-react-dropdown';
import Tilt from 'react-parallax-tilt';
import Lottie from 'react-lottie';
import Dropzone from 'react-dropzone'

import alternative from "../images/alternative.png"
import disco from "../images/disco.png"
import electronic from "../images/electronic.png"
import hiphop from "../images/hip hop.png"
import indie from "../images/indie.png"
import jazz from "../images/jazz.png"
import rock from "../images/rock.png"
import 'react-image-picker/dist/index.css'
import FileTile from "./FileTile";
import midi from "../images/midi.png";
import ProgressButton from "react-progress-button";
import '../button.css'


const styleList = [alternative, disco, electronic, hiphop, indie, jazz, rock];

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

    //todo to access contents of file, use API FileReader, see example in Dropzone documentation
    //new browser privacy settings prevent getting the full file path of the files
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
        //call code to generate file and get download link
        //wait until complete
        //when complete
        this.setState({
            isLoading: true,
            buttonState: 'loading',
        });
        //this.generateRandomMusicRequest()

        //if impossible to use download links download file immediately, will remove download button from result tile...
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