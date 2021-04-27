import React from 'react'
import {Link} from 'react-router-dom'
import midi from "../images/midi.png"

export default function ResultTile({isLoading, hasResult, fileName, downloadLink}) {

    if (!isLoading) {
        if(hasResult) {
            //result with all info
        } else {
            //empty result
        }
    } else {
        //loading animation
    }
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
}