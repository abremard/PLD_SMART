import logo from '../images/logowhite.png'
import {Link} from 'react-router-dom';

import React, {Component} from 'react';
import ResultTile from "./ResultTile";
import ImagePicker from "react-image-picker";
import { Multiselect } from 'multiselect-react-dropdown';


import alternative from "../images/alternative.png"
import disco from "../images/disco.png"
import electronic from "../images/electronic.png"
import hiphop from "../images/hip hop.png"
import indie from "../images/indie.png"
import jazz from "../images/jazz.png"
import rock from "../images/rock.png"
import 'react-image-picker/dist/index.css'
import FileTile from "./FileTile";
import ProgressButton from "react-progress-button";


const styleList = [alternative, disco, electronic, hiphop, indie, jazz, rock];

export default class Scratch1Comp extends Component{
    constructor(props) {
        super(props)
        this.state = {
            image: null,
            artistOptions: [{name: 'Beyonce', id: 1},{name: 'Jay-Z', id: 2},{name: 'Lady Gaga', id: 3},{name: 'Dominic Fike', id: 4}],
            selectedArtists: null,
            instrumentOptions: [{name: 'Guitar', id: 1},{name: 'Piano', id: 2},{name: 'Drums', id: 3},{name: 'Keyboard', id: 4}],
            selectedInstruments: null,
            buttonState: '',
            isLoading: false,
            hasResult:false,
            downloadLink: '',
            fileName: 'New Creation',
        }
        this.onPick = this.onPick.bind(this);
        this.generateFile = this.generateFile.bind(this);
    }

    onPick(image) {
        this.setState({image})
    }

    onSelectArtist(selectedList, selectedItem) {
        this.setState({
            selectedArtists: selectedList
        });
    }

    onRemoveArtist(selectedList, removedItem) {
        this.setState({
            selectedArtists: selectedList
        })
    }

    onSelectInstrument(selectedList, selectedItem) {
        this.setState({
            selectedInstruments: selectedList
        })
    }

    onRemoveInstrument(selectedList, removedItem) {
        this.setState({
            selectedInstruments: selectedList
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
                    <h4>Make from Scratch</h4>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Feugiat viverra molestie quam faucibus viverra nisl. Vitae eget risus, auctor viverra pharetra. Consequat, cras amet, dolor, varius lectus odio libero, leo.</p>
                    <Link to="/scratch5">5 instruments</Link><a style={selectedStyle}>1 instrument</a>
                    <p><br/></p>
                    <ResultTile isLoading={this.state.isLoading} downloadLink={this.state.downloadLink} fileName={this.state.fileName} hasResult={this.state.hasResult}></ResultTile>
                    <h5>Options</h5>
                    <h6>Choose your style</h6>
                    <ImagePicker
                        images ={styleList.map((image, i) => ({src: image, value: i}))}
                        onPick ={this.onPick}
                    />
                    <h6>Choose an artist of inspiration (optional)</h6>
                    <Multiselect
                        options={this.state.artistOptions} // Options to display in the dropdown
                        onSelect={this.onSelect} // Function will trigger on select event
                        onRemove={this.onRemove} // Function will trigger on remove event
                        displayValue="name" // Property name to display in the dropdown op
                        closeIcon = "circle" // tions
                        id="css_custom"
                        style={ {multiselectContainer: {width: '600px'}, searchBox:{color: 'black', border: 'solid white 2px', borderRadius:'0px'}, optionContainer: {backgroundColor: 'black', fontFamily: 'Arial', border: 'solid white 1px', borderRadius: '0px'}, chips: {backgroundColor: '#6EC3F4', fontFamily: 'Arial'}, } }
                    />
                    <h6>Choose an instrument</h6>
                    <Multiselect
                        options={this.state.instrumentOptions} // Options to display in the dropdown
                        onSelect={this.onSelect} // Function will trigger on select event
                        onRemove={this.onRemove} // Function will trigger on remove event
                        displayValue="name" // Property name to display in the dropdown op
                        singleSelect
                        id="css_custom"
                        style={ {multiselectContainer: {width: '600px'}, searchBox:{color: 'black', border: 'solid white 2px', borderRadius:'0px'}, optionContainer: {backgroundColor: 'black', fontFamily: 'Arial', border: 'solid white 1px', borderRadius: '0px'}, chips: {backgroundColor: '#6EC3F4', fontFamily: 'Arial'}, } }
                    />
                    <h6>Maximum Length</h6>
                    <input type="number" name="name" />
                    <h6><br/> </h6>
                    <ProgressButton onClick={this.generateFile} state={this.state.buttonState}>
                        Generate!
                    </ProgressButton>
                    <h5> </h5>
                </div>
            </>
        )

    }
}