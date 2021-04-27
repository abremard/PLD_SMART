import React from 'react'

import scratch from '../images/scratch.png'
import switchimg from '../images/switch.png'
import match from '../images/match.png'
import together from '../images/together.png'
import Navbar from "../components/navbar";
import {Link} from "react-router-dom";
import ResultTile from "../components/ResultTile";

export default function Scratch5() {
    const selectedStyle = {
        color: 'white',
        backgroundColor: 'black',
        border: 'solid white 1px',
        marginBottom: '20px',
    }
    return(
        <>
            <Navbar></Navbar>
            <div className="scratch">
                <Link to="/studio">back to studio</Link>
                <h4>Make from Scratch</h4>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Feugiat viverra molestie quam faucibus viverra nisl. Vitae eget risus, auctor viverra pharetra. Consequat, cras amet, dolor, varius lectus odio libero, leo.</p>
                <a style={selectedStyle}>5 instruments</a><a>1 instrument</a>
                <ResultTile isLoading={false} downloadLink={""} fileName={"File 1"} hasResult={true}></ResultTile>
            </div>
        </>
    )
}