import React from 'react'

import scratch from '../images/scratch.png'
import switchimg from '../images/switch.png'
import match from '../images/match.png'
import together from '../images/together.png'
import Navbar from "../components/navbar";
import {Link} from "react-router-dom";
import ResultTile from "../components/ResultTile";
import ImagePicker from 'react-image-picker'
import Scratch1Comp from "../components/Scratch1Comp";
import MatchComp from "../components/MatchComp";
import JamComp from "../components/JamComp";
//import 'react-image-picker/dist/index.css'



export default function Jam() {


    return(
        <>
            <Navbar></Navbar>
            <JamComp></JamComp>
        </>
    )
}