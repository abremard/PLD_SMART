import React from 'react'

import scratch from '../images/scratch.png'
import switchimg from '../images/switch.png'
import match from '../images/match.png'
import together from '../images/together.png'
import Navbar from "../components/navbar";

export default function StudioMenu() {
    return(
        <>
            <Navbar></Navbar>
            <div className="choose">
                <h4>Choose a mode</h4>
                <table>
                    <tr>
                        <td>
                            <img src={scratch}/>
                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Feugiat viverra molestie
                                    quam faucibus viverra nisl. Vitae eget risus, auctor viverra pharetra. Consequat,
                                    cras amet, dolor, varius lectus odio libero, leo. Ultrices tristique ullamcorper
                                    fermentum lacus diam proin sagittis, ac.</p>
                                <a href="">Let's Go!</a>
                        </td>
                        <td>
                            <img src={together}/>
                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Feugiat viverra molestie
                                    quam faucibus viverra nisl. Vitae eget risus, auctor viverra pharetra. Consequat,
                                    cras amet, dolor, varius lectus odio libero, leo. Ultrices tristique ullamcorper
                                    fermentum lacus diam proin sagittis, ac.</p>
                                <a href="">Let's Go!</a>
                        </td>
                        <td>
                            <img src={match}/>
                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Feugiat viverra molestie
                                    quam faucibus viverra nisl. Vitae eget risus, auctor viverra pharetra. Consequat,
                                    cras amet, dolor, varius lectus odio libero, leo. Ultrices tristique ullamcorper
                                    fermentum lacus diam proin sagittis, ac.</p>
                                <a href="">Let's Go!</a>
                        </td>
                        <td>
                            <img src={switchimg}/>
                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Feugiat viverra molestie
                                    quam faucibus viverra nisl. Vitae eget risus, auctor viverra pharetra. Consequat,
                                    cras amet, dolor, varius lectus odio libero, leo. Ultrices tristique ullamcorper
                                    fermentum lacus diam proin sagittis, ac.</p>
                                <a href="">Let's Go!</a>
                        </td>
                    </tr>
                </table>
            </div>
        </>
    )
}