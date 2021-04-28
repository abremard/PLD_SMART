import logo from '../images/logowhite.png'
import {Link} from 'react-router-dom';

import React, {Component} from 'react';
import ResultTile from "./ResultTile";
import ImagePicker from "react-image-picker";
import { Multiselect } from 'multiselect-react-dropdown';
import { saveAs } from 'file-saver';

import alternative from "../images/alternative.png"
import disco from "../images/disco.png"
import electronic from "../images/electronic.png"
import hiphop from "../images/hip hop.png"
import indie from "../images/indie.png"
import jazz from "../images/jazz.png"
import rock from "../images/rock.png"
import 'react-image-picker/dist/index.css'
import Navbar from "./navbar";


const styleList = [alternative, disco, electronic, hiphop, indie, jazz, rock];

export default class Scratch5Comp extends Component{

    constructor(props) {
        super(props);
        this.state = {
            isLoading: false,
            hasResult:false,
            downloadLink: '',
            fileName: 'New Creation',
        }
        this.generateFile = this.generateFile.bind(this);
    }

    generateRandomMusicRequest = async (long) => {
        const url ='http://37ce43fd24b2.ngrok.io/api/v1/compose/polyphonic/musegan/v0'
        this.setState({
            isLoading: true,
        });
        fetch(url)
        .then( res => res.blob() )
        .then( blob => saveAs(blob, 'music.mid'))
        .then(() => {this.setState({
            isLoading: false,
            hasResult: true,
            downloadLink: '' //insert download link...,
        })})
    }
    generateFile() {
        
        //call code to generate file and get download link
        //wait until complete
        //when complete
        this.generateRandomMusicRequest()
        
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
                    <h4>Make from Scratch</h4>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Feugiat viverra molestie quam faucibus viverra nisl. Vitae eget risus, auctor viverra pharetra. Consequat, cras amet, dolor, varius lectus odio libero, leo.</p>
                    <a style={selectedStyle}>5 instruments</a><Link to="/scratch1">1 instrument</Link>
                    <ResultTile isLoading={this.state.isLoading} downloadLink={this.state.downloadLink} fileName={this.state.fileName} hasResult={this.state.hasResult}></ResultTile>
                    <a style={generateStyle} onClick={this.generateFile}> Generate</a>
                </div>
            </>
        )

    }
}