import logo from '../images/logowhite.png'
import {Link} from 'react-router-dom';

import React, {Component} from 'react';

export default class Navbar extends Component {
    render() {
        return (
            <div className="appbar">
                <div className="applogo">
                    <img src={logo} width="80px"/>
                        <p>ilolio music studio</p>
                </div>
                <Link to="/">
                    Home
                </Link>
            </div>
        );
    }
}