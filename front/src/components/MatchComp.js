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





const styleList = [alternative, disco, electronic, hiphop, indie, jazz, rock];

export default class MatchComp extends Component{
    constructor(props) {
        super(props)
        this.state = {
            files: [],
        }
        this.onDrop = this.onDrop.bind(this);
    }

    //todo to access contents of file, use API FileReader, see example in Dropzone documentation
    //new browser privacy settings prevent getting the full file path of the files
    onDrop(acceptedFiles){
        console.log(acceptedFiles);
        this.setState(state => {
            return {
                files: acceptedFiles,
            };
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


        console.log(this.state.filenames);

        return(
            <>
                <div className="scratch">
                    <Link to="/studio">back to studio</Link>
                    <h4>Perfect Match</h4>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Feugiat viverra molestie quam faucibus viverra nisl. Vitae eget risus, auctor viverra pharetra. Consequat, cras amet, dolor, varius lectus odio libero, leo.</p>
                    <ResultTile isLoading={true} downloadLink={""} fileName={"File 1"} hasResult={true}></ResultTile>
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
                                            <p>Drag 'n' drop some files here, or click to select files</p>
                                        </div>
                                    </div>
                                </section>
                            )}
                        </Dropzone>
                    </div>

                    <h6><br/> </h6>
                    <a style={generateStyle}> Generate</a>
                    <h5> </h5>
                </div>
            </>
        )

    }
}