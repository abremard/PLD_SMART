import React, {Component} from 'react';
import {Link} from 'react-router-dom';

import Dropzone from 'react-dropzone'
import Slider, {Handle, SliderTooltip} from 'rc-slider';
import {toast} from "react-hot-toast";
import ProgressButton from "react-progress-button";

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
import '../slider.css';

export default class TogetherComp extends Component{
    constructor(props) {
        super(props)
        this.state = {
            files: [],
            buttonState: '',
            isLoading: false,
            hasResult:false,
            downloadLink: '',
            fileName: 'New Creation',
            length: 50,
            balance: 50
        }
        this.onDrop = this.onDrop.bind(this);
        this.generateFile = this.generateFile.bind(this);
        this.onChangeLength = this.onChangeLength.bind(this);
        this.onChangeBalance = this.onChangeBalance.bind(this);
    }

    onDrop(acceptedFiles){
        console.log(acceptedFiles);
        var filesTemp = this.state.files;
        acceptedFiles.forEach(item => {
            if (filesTemp.length<2) {
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
        //get files
        this.state.files.forEach((file) => {
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
        })
        //call code to generate file and get download link
        //wait until complete
        //when complete
        this.setState({
            isLoading: true,
            buttonState: 'loading',
        });

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
            marginBottom: '20px',
        };
        const generateStyle = {
            padding: '20px',
        };
        return(
            <>
                <div className="scratch">
                    <Link to="/studio">back to studio</Link>
                    <h4>Bring Together</h4>
                    <p>Bring your favorite two musical pieces together. Upload two midi files and our
                        algorithm will interpolate and create two original mash-ups of your uploaded music. Choose
                        the length and the balance of your mashup for the perfect result.</p>
                    <div className="files">
                        <ResultTile isLoading={this.state.isLoading} downloadLink={this.state.downloadLink} fileName={"File 1 into File 2"} hasResult={this.state.hasResult}></ResultTile>
                        <ResultTile isLoading={this.state.isLoading} downloadLink={this.state.downloadLink} fileName={"File 2 into File 1"} hasResult={this.state.hasResult}></ResultTile>
                    </div>
                    <h5>Upload your files</h5>
                    <div className="files">
                        {this.state.files.map(item => (
                            <FileTile fileName={item.name} downloadLink={""}></FileTile>
                        ))}
                        {this.state.files.length == 2 ?
                            <p></p>
                            : <Dropzone onDrop={this.onDrop}>
                                {({getRootProps, getInputProps}) => (
                                    <section>
                                        <div className="tile" {...getRootProps()}>
                                            <h4>Upload File</h4>
                                            <div className="zone">
                                                <input {...getInputProps()} />
                                                <p>Drag & drop up your 2 files here, or click to select files</p>
                                            </div>
                                        </div>
                                    </section>
                                )}
                            </Dropzone>}
                    </div>
                    <h5>Options</h5>
                    <h6>Length</h6>
                    <Slider min={0} max={500} defaultValue={50} handle={handle} step={10} onChange={value => {this.setState({length: value})}} />
                    <h6>Balance of Mix</h6>
                    <Slider min={0} max={100} defaultValue={50} handle={handle} step={10} onChange={value => {this.setState({balance : value})}}/>
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