import Player from '../components/Player'
import Navbar from '../components/navbar'
import ProgressButton from "react-progress-button";


import '@magenta/music';
import 'focus-visible';

// add navbar etc here but for the moment player overlaps everything
export default function MidiDemo() {

    return(
       <div>
            <Navbar/>
            <Player/>
            <ProgressButton >
                        download
            </ProgressButton>
       </div>
    )
}