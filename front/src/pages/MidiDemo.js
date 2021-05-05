import React, { useState, useEffect } from 'react';
import Player from '../components/Player'
import Navbar from '../components/navbar'
import {Link, useParams} from 'react-router-dom';
import { saveAs } from 'file-saver';

// add navbar etc here but for the moment player overlaps everything
export default function MidiDemo() {

    let {url} = useParams();
    const decUrl = url.replaceAll('_','/');
    console.log("DECODED "+ decUrl);
    // put this url if you want to test only the midi player
    //url = 'https://cdn.jsdelivr.net/gh/cifkao/html-midi-player@2b12128/jazz.mid';
    console.log(url)

    return(
       <div>
            <Navbar/>
            <Player url={decUrl}/>
       </div>
    )
}
