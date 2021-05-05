import React, { useState, useEffect } from 'react';
import Player from '../components/Player'
import Navbar from '../components/navbar'
import ProgressButton from "react-progress-button";
import { useParams } from "react-router";
import {Link} from 'react-router-dom';


const superagent = require('superagent');

// jazz.mid

// add navbar etc here but for the moment player overlaps everything
export default function MidiDemo(props) {

    let {url} = useParams();
    url = 'https://cdn.jsdelivr.net/gh/cifkao/html-midi-player@2b12128/' + url;
    console.log(url)

    return( 
       <div>
            <Navbar/>
            <Link to="/studio">back to studio</Link>
            <Player url={url}/>
       </div>
    )
}
