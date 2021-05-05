import React, {Component} from 'react';
import {Link} from 'react-router-dom';

import { saveAs } from 'file-saver';
import {toast, Toaster} from "react-hot-toast";
import ProgressButton from "react-progress-button";
import Slider, {Handle, SliderTooltip} from "rc-slider";

import ResultTile from "./ResultTile";

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
const superagent = require('superagent');
export default class Scratch5Comp extends Component{

    constructor(props) {
        super(props);
        this.state = {
            isLoading: false,
            hasResult:false,
            downloadLink: '',
            fileName: 'New Creation',
            buttonState: '',
            chords: 0,
            style: 0,
            melodyDrums: 0,
            melodyPiano: 0,
            melodyBass: 0,
            melodyGuitar: 0,
            melodyStrings: 0,
            grooveDrums: 0,
            groovePiano: 0,
            grooveBass: 0,
            grooveGuitar: 0,
            grooveStrings: 0,
        }
        this.generateFile = this.generateFile.bind(this);
    }
    

    generateRandomMusicRequest = async (long) => {
        var servername;
        const response = await superagent.get('http://127.0.0.1:5000/')
        servername = JSON.parse(response.text).idd
        const url =`${(servername)}/api/v1/compose/polyphonic/musegan/v0/dev-tmp?chords=${(this.state.chords)}&style=${(this.state.style)}&melody_drum=${(this.state.melodyDrums)}&melody_piano=${(this.state.melodyPiano)}&melody_guitar=${(this.state.melodyGuitar)}&melody_bass=${(this.state.melodyBass)}&melody_strings=${(this.state.melodyStrings)}&groove_drum=${(this.state.grooveDrums)}&groove_piano=${(this.state.groovePiano)}&groove_guitar=${(this.state.grooveGuitar)}&groove_bass=${(this.state.grooveBass)}&groove_strings=${(this.state.grooveStrings)}`
        //todo catch error
        fetch(url)
        .then( res => res.blob() )
        .then( blob => saveAs(blob, 'music.mid'))
        .then(() => {this.setState({
            isLoading: false,
            buttonState: 'success',
            hasResult: true,
            downloadLink: '' //insert download link...,
        })}).catch(() => {
                toast.error("Something went wrong. Please try again later");
                this.setState({
                    isLoading: false,
                    buttonState: 'error',
                    hasResult: false,
                });
            }
        )
    }
    generateFile() {
        this.setState({
            isLoading: true,
            buttonState: 'loading',
        });
        this.generateRandomMusicRequest()
    }

    render() {
        const handle = props => {
            const { value, dragging, index, ...restProps } = props;
            return (
                <SliderTooltip
                    prefixCls="rc-slider-tooltip"
                    overlay={`${value}`}
                    visible={dragging}
                    placement="top"
                    key={index}
                >
                    <Handle value={value} {...restProps} />
                </SliderTooltip>
            );
        };
        const selectedStyle = {
            color: 'white',
            backgroundColor: 'black',
            border: 'solid white 1px',
            marginBottom: '100px',
        };
        return(
            <>
                <div className="toaster"><Toaster/></div>
                <div className="scratch">
                    <Link to="/studio">back to studio</Link>
                    <h4>Make from Scratch</h4>
                    <p>Create a completely new musical piece with one or multiple instruments. Choose
                        between multiple musical styles, artists of inspiration, and types of instruments
                        to make every unique piece your own. Uses the MuseGAN and LSTM algorithms.</p>
                    <a style={selectedStyle}>5 instruments</a><Link to="/scratch1">1 instrument</Link>
                    <p><br/></p>
                    <ResultTile isLoading={this.state.isLoading} downloadLink={this.state.downloadLink} fileName={this.state.fileName} hasResult={this.state.hasResult}></ResultTile>
                    <h5>Options</h5>
                    <div className="maxislider">
                        <h6>Chords</h6>
                        <Slider min={-10} max={10} defaultValue={0} handle={handle} step={1} onChange={value => {this.setState({chords: value})}} />
                    </div>
                    <div className="maxislider">
                        <h6>Style</h6>
                        <Slider min={-10} max={10} defaultValue={0} handle={handle} step={1} onChange={value => {this.setState({style: value})}}/>
                    </div>
                    <h6>Melody</h6>
                    <div className="files">
                        <div className="minislider">
                            <p>Drums</p>
                            <Slider min={-10} max={10} defaultValue={0} handle={handle} step={1} onChange={value => {this.setState({melodyDrums: value})}}/>
                        </div>
                        <div className="minislider">
                            <p>Piano</p>
                            <Slider min={-10} max={10} defaultValue={0} handle={handle} step={1} onChange={value => {this.setState({melodyPiano: value})}}/>
                        </div>
                        <div className="minislider">
                            <p>Guitar</p>
                            <Slider min={-10} max={10} defaultValue={0} handle={handle} step={1} onChange={value => {this.setState({melodyGuitar: value})}}/>
                        </div>
                        <div className="minislider">
                            <p>Bass</p>
                            <Slider min={-10} max={10} defaultValue={0} handle={handle} step={1} onChange={value => {this.setState({melodyBass: value})}}/>
                        </div>
                        <div className="minislider">
                            <p>Strings</p>
                            <Slider min={-10} max={10} defaultValue={0} handle={handle} step={1} onChange={value => {this.setState({melodyStrings: value})}}/>
                        </div>
                    </div>
                    <h6>Groove</h6>
                    <div className="files">
                        <div className="minislider">
                            <p>Drums</p>
                            <Slider min={-10} max={10} defaultValue={0} handle={handle} step={1} onChange={value => {this.setState({grooveDrums: value})}}/>
                        </div>
                        <div className="minislider">
                            <p>Piano</p>
                            <Slider min={-10} max={10} defaultValue={0} handle={handle} step={1} onChange={value => {this.setState({groovePiano: value})}}/>
                        </div>
                        <div className="minislider">
                            <p>Guitar</p>
                            <Slider min={-10} max={10} defaultValue={0} handle={handle} step={1} onChange={value => {this.setState({grooveGuitar: value})}}/>
                        </div>
                        <div className="minislider">
                            <p>Bass</p>
                            <Slider min={-10} max={10} defaultValue={0} handle={handle} step={1} onChange={value => {this.setState({grooveBass: value})}}/>
                        </div>
                        <div className="minislider">
                            <p>Strings</p>
                            <Slider min={-10} max={10} defaultValue={0} handle={handle} step={1} onChange={value => {this.setState({grooveStrings: value})}}/>
                        </div>
                    </div>
                    <p><br/></p>
                    <ProgressButton onClick={this.generateFile} state={this.state.buttonState}>
                        Generate
                    </ProgressButton>
                    <br/><br/>
                </div>
            </>
        )
    }
}