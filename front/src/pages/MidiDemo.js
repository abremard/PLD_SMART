import React, { useState, useEffect } from 'react';
import Player from '../components/Player'
import Navbar from '../components/navbar'
import ProgressButton from "react-progress-button";
import { useParams } from "react-router";
import {Link} from 'react-router-dom';


import 'focus-visible';

// add navbar etc here but for the moment player overlaps everything
export default function MidiDemo() {

    return(
       <div>
            <Navbar/>
            <Player url="https://cdn.jsdelivr.net/gh/cifkao/html-midi-player@2b12128/jazz.mid"/>
            <ProgressButton >
                        download
            </ProgressButton>
       </div>
    )
}