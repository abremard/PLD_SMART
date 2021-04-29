import React from 'react'

import logo from '../images/logowhitetext.png'
import illustration from '../images/illustration.png'
import scratch from '../images/scratch.png'
import switchimg from '../images/switch.png'
import match from '../images/match.png'
import together from '../images/together.png'
import {Link} from "react-router-dom";

export default function Home() {

    let elem = document.querySelector("#parallax");

    window.addEventListener('mousemove', (e) => {

        elem = document.querySelector("#parallax");
        let _w = window.innerWidth / 2;
        let _h = window.innerHeight / 2;
        let _mouseX = e.clientX;
        let _mouseY = e.clientY;
        let _depth1 = `${50 - (_mouseX - _w) * 0.01}% ${
            50 - (_mouseY - _h) * 0.01
        }%`;
        let _depth2 = `${50 - (_mouseX - _w) * 0.02}% ${
            50 - (_mouseY - _h) * 0.02
        }%`;
        let _depth3 = `${50 - (_mouseX - _w) * 0.06}% ${
            50 - (_mouseY - _h) * 0.06
        }%`;
        let x = `${_depth3}, ${_depth2}, ${_depth1}`;
        console.log(x);
        if (elem!= null) {
            elem.style.backgroundPosition = x;
        }
    })

    return(
        <body>
        <div className="header">
            <div id="parallax">
                <div className="navbar">
                    <div className="logo">
                        <img src={logo} width="120px"/>
                    </div>
                    <Link to="/studio">My Studio</Link>
                </div>
                <div className="title">
                    <h1>Endless Opportunities.</h1>
                    <h2>Great Music.</h2>
                </div>
            </div>

        </div>
        <div className="text">
            <p>Creating music just got much easier. Ilolio Music Lab offers you creation tools
            that help you find inspiration, generate new ideas, create unique compositions
            for your musical projects, or play with music. Ilolio is your ultimate co-writer, co-producer and co-musical genius.</p>
        </div>
        <div className="works">
            <h3>How it works</h3>
            <img src={illustration}/>
                <p>Ilolio Music lab uses a combination of multiple machine learning algorithms to offer you multiple
                music creation tools. The algorithms take into account your own files and customizations of different
                parameters to create unique musical compositions. Anyone can create with Ilolio - the simple interface
                is easy to navigate and understand.</p>
        </div>
        <div className="services">
            <h3>What can you do</h3>
            <table>
                <tr>
                    <td>
                        <img src={scratch}/>
                            <p>Create a completely new musical piece with one or multiple instruments. Choose
                                between multiple musical styles, artists of inspiration, and types of instruments
                                to make every unique piece your own. Uses the MuseGAN and LSTM algorithms.</p>
                    </td>
                    <td>
                        <img src={together}/>
                            <p>Bring your favorite two musical pieces together. Upload two midi files and our
                                algorithm will interpolate and create two original mash-ups of your uploaded music. Choose
                                the length and the balance of your mashup for the perfect result.</p>
                    </td>
                    <td>
                        <img src={match}/>
                            <p>Create a completely new musical piece using your own favorite sounds as the inspiration.
                                Upload up to 10 midi files of your choosing - any style, any artist, any instrument. Ilolio
                                will create a brand new midi file inspired by your uploads. Uses the LSTM algorithm.</p>
                    </td>
                    <td>
                        <img src={switchimg}/>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Feugiat viverra molestie quam
                                faucibus viverra nisl. Vitae eget risus, auctor viverra pharetra. Consequat, cras amet,
                                dolor, varius lectus odio libero, leo. Ultrices tristique.</p>
                    </td>
                </tr>
            </table>
        </div>
        <div className="ready">
            <h3>Ready?</h3>
            <Link to="/studio">Let's Go!</Link>
        </div>
        <div className="text">
            <p>2021, Ilolio Music Lab. Created by Heptanome.</p>
            <p style={{fontSize: 10}}>Stefan Ristovski, Alexandre Bremard, Emma Neiss, Yann Dupont, Alexis Shan Yan, Iyad Tout, Aydin Akaydin</p>
        </div>

        </body>
    )
}