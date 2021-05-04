import React from 'react'

import scratch from '../images/scratch.png'
import jam from '../images/jam.png'
import match from '../images/match.png'
import together from '../images/together.png'
import Navbar from "../components/navbar";
import {Link} from "react-router-dom";

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
                                <p>Create a completely new musical piece with one or multiple instruments. Choose
                                    between multiple musical styles, artists of inspiration, and types of instruments
                                    to make every unique piece your own. Uses the MuseGAN and LSTM algorithms.</p>
                                <Link to="/scratch5">Let's Go!</Link>
                        </td>
                        <td>
                            <img src={together}/>
                                <p>Bring your favorite two musical pieces together. Upload two midi files and our
                                    algorithm will interpolate and create two original mash-ups of your uploaded music. Choose
                                    the length and the balance of your mashup for the perfect result.</p>
                                <Link to="/together">Let's Go!</Link>
                        </td>
                        <td>
                            <img src={match}/>
                                <p>Create a completely new musical piece using your own favorite sounds as the inspiration.
                                    Upload up to 10 midi files of your choosing - any style, any artist, any instrument. Ilolio
                                    will create a brand new midi file inspired by your uploads. Uses the LSTM algorithm.
                                </p>
                                <Link to="/match">Let's Go!</Link>
                        </td>
                        <td>
                            <img src={jam}/>
                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Feugiat viverra molestie
                                    quam faucibus viverra nisl. Vitae eget risus, auctor viverra pharetra. Consequat,
                                    cras amet, dolor, varius lectus odio libero, leo. Ultrices tristique ullamcorper
                                    fermentum lacus diam proin sagittis, ac.</p>
                                <Link to="/jam">Let's Go!</Link>
                        </td>
                    </tr>
                </table>
            </div>
        </>
    )
}