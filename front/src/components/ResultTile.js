import React from 'react'
import {Link} from 'react-router-dom'
import midi from "../images/midi.png"
import { useLoading, Grid } from '@agney/react-loading';
import Tilt from "react-parallax-tilt";
import Lottie from "react-lottie";
import animationData from "../images/check.json";


export default function ResultTile({isLoading, hasResult, fileName, downloadLink}) {

    const selectedStyle = {
        backgroundColor: '#6EC3F4',
    }
    const animationOptions = {
        loop: false,
        autoplay: true,
        animationData: animationData,
        rendererSettings: {
            preserveAspectRatio: "xMidYMid slice"
        }
    };

    if (!isLoading) {
        if(hasResult) {
            //result with all info
            return (
                <div className="tile">
                    <h4>Result</h4>
                    <div className="metadata">
                        <h5>{fileName}</h5>
                        <Link to={`/demo/${(downloadLink)}/`}>Preview</Link>
                    </div>
                    <div className="checkmark">
                        <Tilt className="parallax-effect" perspective={2000}>
                            <Lottie
                                options={animationOptions}
                                height={80}
                                width={80}
                            />
                        </Tilt>

                    </div>
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
                <div className="checkmark">
                    <Tilt className="parallax-effect" perspective={2000}>
                        <Grid width="60"/>
                    </Tilt>
                </div>
            </div>
        )
    }
}