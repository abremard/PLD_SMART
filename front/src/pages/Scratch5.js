import React from 'react'

import scratch from '../images/scratch.png'
import switchimg from '../images/switch.png'
import match from '../images/match.png'
import together from '../images/together.png'
import Navbar from "../components/navbar";
import {Link} from "react-router-dom";
import ResultTile from "../components/ResultTile";
import Scratch5Comp from "../components/Scratch5Comp";

export default function Scratch5() {
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
            <Navbar></Navbar>
            <Scratch5Comp></Scratch5Comp>
        </>
    )
}