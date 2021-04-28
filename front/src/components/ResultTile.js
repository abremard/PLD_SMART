import React from 'react'
import {Link} from 'react-router-dom'
import midi from "../images/midi.png"
import { useLoading, Grid } from '@agney/react-loading';


export default function ResultTile({isLoading, hasResult, fileName, downloadLink}) {

    

    const selectedStyle = {
        backgroundColor: '#6EC3F4',
    }

    if (!isLoading) {
        if(hasResult) {
            //result with all info
            return (
                <div className="tile">
                    <h4>Result</h4>
                    <div className="metadata">
                        <h5>{fileName}</h5>
                        <p>0:15</p>
                    </div>
                    <a>Download .midi</a>
                </div>
            )
        } else {
            return(
                <div className="tile">
                    <h4>Result</h4>
                    <div className="metadata">
                        <h5>Nothing to see here...</h5>
                        <p>Generate a piece and it will appear here</p>
                    </div>
                </div>
            )
        }
    } else {
        //loading animation
        return(
            <div className="tile" style={selectedStyle}>
            <h4>Result</h4>
            <div className="metadata">
                <h5>Generating...</h5>
            </div>
            <Grid width="60"/>
        </div>
        )
    }
}