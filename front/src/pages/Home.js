import React from 'react'

import logo from '../images/logowhitetext.png'
import illustration from '../images/illustration.png'
import scratch from '../images/scratch.png'
import switchimg from '../images/switch.png'
import match from '../images/match.png'
import together from '../images/together.png'

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
        elem.style.backgroundPosition = x;
    })

    return(
        <body>
        <div className="header">
            <div id="parallax">
                <div className="navbar">
                    <div className="logo">
                        <img src={logo} width="120px"/>
                    </div>
                    <a href="">My Studio</a>
                </div>
                <div className="title">
                    <h1>Endless Opportunities.</h1>
                    <h2>Great Music.</h2>
                </div>
            </div>

        </div>
        <div className="text">
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Feugiat viverra molestie quam faucibus viverra
                nisl. Vitae eget risus, auctor viverra pharetra. Consequat, cras amet, dolor, varius lectus odio libero,
                leo. Ultrices tristique ullamcorper fermentum lacus diam proin sagittis, ac.</p>
        </div>
        <div className="works">
            <h3>How it works</h3>
            <img src={illustration}/>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Feugiat viverra molestie quam faucibus
                    viverra nisl. Vitae eget risus, auctor viverra pharetra. Consequat, cras amet, dolor, varius lectus
                    odio libero, leo. Ultrices tristique ullamcorper fermentum lacus diam proin sagittis, ac.</p>
        </div>
        <div className="services">
            <h3>What can you do</h3>
            <table>
                <tr>
                    <td>
                        <img src={scratch}/>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Feugiat viverra molestie quam
                                faucibus viverra nisl. Vitae eget risus, auctor viverra pharetra. Consequat, cras amet,
                                dolor, varius lectus odio libero, leo. Ultrices tristique ullamcorper fermentum lacus
                                diam proin sagittis, ac.</p>
                    </td>
                    <td>
                        <img src={together}/>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Feugiat viverra molestie quam
                                faucibus viverra nisl. Vitae eget risus, auctor viverra pharetra. Consequat, cras amet,
                                dolor, varius lectus odio libero, leo. Ultrices tristique ullamcorper fermentum lacus
                                diam proin sagittis, ac.</p>
                    </td>
                    <td>
                        <img src={match}/>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Feugiat viverra molestie quam
                                faucibus viverra nisl. Vitae eget risus, auctor viverra pharetra. Consequat, cras amet,
                                dolor, varius lectus odio libero, leo. Ultrices tristique ullamcorper fermentum lacus
                                diam proin sagittis, ac.</p>
                    </td>
                    <td>
                        <img src={switchimg}/>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Feugiat viverra molestie quam
                                faucibus viverra nisl. Vitae eget risus, auctor viverra pharetra. Consequat, cras amet,
                                dolor, varius lectus odio libero, leo. Ultrices tristique ullamcorper fermentum lacus
                                diam proin sagittis, ac.</p>
                    </td>
                </tr>
            </table>
        </div>
        <div className="ready">
            <h3>Ready?</h3>
            <a href="">Let's Go!</a>
        </div>

        </body>
    )
}