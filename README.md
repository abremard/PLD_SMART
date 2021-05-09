# PLD_SMART

## Description

A web application to generate music, with 5 different functionnalities :
- From Scratch (5 instruments) lets you generate a multi-track song from scratch.
- From Scratch (1 instrument) lets you generate a single-track song by picking reference songs sorted by genre and artist.
- Perfect Match lets you generate a single-track song by training a neural network from the ground-up with 1 to 5 Midi files given as input.
- Bring Together lets you interpolate between two Midi files given as input.
- Jam Session lets you generate a single-track song from a list of chords, and the option to continue a Midi file given as input.

## Requirements

### Frontend

The projects requires Node.js, which you can download from https://nodejs.org/en/download/ .
It was developped with Node.js 14.16.1, other versions have not been tested.

### Backend and Algo

The whole project runs on python 3.6.5, so make sure you have the correct version installed, or use anaconda to create a virtual environment with the proper python version.

Requirements files are contained in the `requirements/{venv name}/requirements.txt file`

The default virtual environment should be `pld-smart`
> Notes: `musegan` virtual environment is a sandbox for musegan v1, only use this when developping musegan v1

In development mode, use virtual environment. To setup one, simply run the
```
python -m venv {venv name}
```

To install requirements, first activate your virtual environment:

For Linux/Mac, run
```
venv/{venv name}/Scripts/activate
```

For Windows, run
```
venv/{venv name}/Scripts/Activate.ps1
```

Then install the requirements given in the requirements.txt file
```
pip install -r requirements/{venv name}/requirements.txt
```


## Running the app

There are two scripts to automatize running the app :
- [init_app.bat] sets the project up, by installing required python and npm packages. It only needs to be run once, or if there are new commits.
- [run_app.bat] starts npm and flask, and opens the app in the default browser. It can be opened from any browser at [localhost:3000].


## Frontend

The Frontend uses NodeJs and React. For this prototype version, the backend's flask server address changes after 30 minutes. We store the last address in a Firebase database with every new run of the flask server. Thus, we also need to dynamically retrieve this address before every request to the notebook back-end. To this aim, we run a light flask server on the client side that can communicate with the firebase database to retrieve the backend's flask server current address before every request. Note that the need for this server will be gone once the project is permanently deployed on a fixed address: the API requests will simply begin with said fixed address.

## Backend

The project uses a flask server on a notebook as back-end, which has API routes set-up, each answering to requests to generate music and other utilities. The back-end also communicates with the database, to display the list of songs for the From Scratch (1 instrument) option and to write/read generated files.

## Database

Scripts and stuff for pre-processing MIDI files, uploading them & their metadata to the Firebase database/storage and for editing the database content.

*Warning: to use these scripts, you need write access to our Firebase database. If you don't know where to find the `creds.json` file mentioned below, 
then either you forgot to read the pinned messages and should head to our Discord server, or you are not supposed to have write access to our database.
If in the second case, you can skip this section as it won't be of any use for you.*

### Firestore
Requirements to use Python scripts to edit the Firestore database (tested on Python 3.8):
 - copy the `cred.json` I sent you into `src/database/firestore/` (:warning: : NEVER commit this file on VCS, it contains credentials giving write access to the DB)
 - install the required modules : (requires pip to work):
 ```shell script
> pip install firebase_admin unidecode
```

### Metadata processing
Requirements to use Python scripts wih Spotify's API (tested on Python 3.8):
 - copy the `spotify_credentials.txt` I sent you into `src/database/metadata_processing/` (:warning: : NEVER commit this file on VCS, it contains our unique API credentials)
 - install the required modules : (requires pip to work):
 ```shell script
> pip install spotipy mido
```

### Useful scripts
 - **upload MIDI files** to Firebase: 
 ```shell script
> python src/database/__init__.py <path/to/MIDI/root> [genre_of_midi_files]
```
**Input requirements**: 
 - `path/to/MIDI/folders/root` should only contain MIDI files in subdirectories named as the files' artist. 
Each artist folder will result in an artist entry in the database (new data will be appended to the existing data if the artist alraedy exists).
 - MIDI file names should contain an instrument name in `("guitar", "drums", "piano", "bass", "strings")` (if it is not already the case, see `src/database/metadata_processing/sort_functions.py`)

Example hierarchy:
```
upload_from_here/
    | -- ACDC/
        | -- hells_bells_guitar.mid    
        | -- hells_bells_drums.mid
    | -- Dream Theater/
        | -- dance_of_eternity_piano.mid
        | -- dance_of_eternity_drums.mid
        | -- the_count_of_tuscany_strings.mid
```

-> If not provided, the script will fetch a genre for each artist folder using Spotify API (chooses the first genre provided, usually not the best)
-> It is recommended to upload files of the same genre in the same run and specify the genre to avoid Spotify API randomness...
:warning: Uploading files takes some time, dont upload too many files at once (limit yourself to a few hundred files a run)


 - **renaming a genre** (typically if you didn't provide a genre for your MIDI files and Spotify returned you a weird genre):
```shell script
> python src/database/firestore/db_postprocessing.py <genre_to_rename> <new_genre_name>
```
-> Renames the first genre provided as the second


## Algo

This project implements interfaces for 4 different neural networks :
- MuseGAN for the From Scratch (5 instruments) option : Hao-Wen Dong, et al. "MuseGAN: Multi-track Sequential Generative Adversarial Networks for Symbolic Music Generation and 
Accompaniment." (2017)
- LSTM with attention mechanism for the  From Scratch (1 instrument) and Perfect Match options : [https://github.com/davidADSP/GDL_code], [https://github.com/davidADSP/GDL_code/blob/master/models/RNNAttention.py]
- MusicVAE by Google Magenta for the Bring Together option : https://github.com/magenta/magenta/tree/master/magenta/models/music_vae
- ImprovRNN by Google Magenta for the Jam Session option : https://github.com/magenta/magenta/tree/master/magenta/models/improv_rnn

