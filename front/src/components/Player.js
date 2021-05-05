import React,{ Component } from 'react'
import 'html-midi-player'
import InnerHTML from 'dangerously-set-html-content'
import { ThreeDots } from '@agney/react-loading';
import {Link} from 'react-router-dom';

class Player extends Component{

    constructor(props){
        super();
        this.visRef = React.createRef();
        this.playRef = React.createRef();
    }

    componentDidMount(){
        var vis = this.visRef.current
        vis.config = {
            noteHeight: 4,
            pixelsPerTimeStep: 60,
          };
    }

    render() {
        return (
            <section id="section3">
                <><InnerHTML html={this.getHTML(this.props.url)}/></>
                <div id="rotatedDiv">
                    <midi-visualizer 
                        ref={this.visRef}
                        type="waterfall" 
                        id="myPianoRollVisualizer"
                        src={this.props.url}>
                    </midi-visualizer>
                </div>
            </section>
        )
    }

    getHTML(url){
        const htmlScript = "<head><script src='https://cdn.jsdelivr.net/combine/npm/tone@14.7.58,npm/@magenta/music@1.21.0/es6/core.js,npm/focus-visible@5'></script></head>"
        const htmlBody = "<div>"
        + "<midi-player "
        + "ref={this.playRef} "
        +"src='"+ url +"'"
        +" sound-font='https://drive.google.com/drive/folders/1gnbAgMs5KQE8Yt-ickAzF1p-hv7xt_cs' visualizer='#myPianoRollVisualizer'>"
        +"</midi-player>"
        +"</div>";

        console.log(htmlScript + htmlBody);
        return htmlScript + htmlBody;
    }
}

export default Player
