import React, { useState, useEffect } from 'react';
import Player from '../components/Player'
import Navbar from '../components/navbar'
import {Link, useParams} from 'react-router-dom';

// add navbar etc here but for the moment player overlaps everything
export default function MidiDemo() {

    let {url} = useParams();
    //url = 'https://cdn.jsdelivr.net/gh/cifkao/html-midi-player@2b12128/jazz.mid'; //+ url;
    const decUrl = url.replaceAll('_','/');
    console.log("DECODED "+ decUrl);

    console.log(url)

    return(
       <div>
            <Navbar/>
            <Player url={decUrl}/>
       </div>
    )
}

//https://storage.googleapis.com/ilolio.appspot.com/Generated/output-20210505-125450.mid
f0ac6a2d63b246875d77f95f24d96357af78
