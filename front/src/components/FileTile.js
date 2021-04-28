import React from 'react'
import {Link} from 'react-router-dom'
import midi from "../images/midi.png"
import { useLoading, Grid } from '@agney/react-loading';
import { saveAs } from 'file-saver';

export default function FileTile({fileName, downloadLink}) {

    const selectedStyle = {
        backgroundColor: '#6EC3F4',
    }

    return (
        <div className="tile">
            <h4>MIDI File</h4>
            <img src={midi} width={'50px'}/>
            <div className="metadata">
                <h5>{fileName}</h5>
                <p>0:15</p>
            </div>
        </div>
    )
}