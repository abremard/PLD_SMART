# PLD_SMART

## Description

## Frontend

## Backend

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

## Requirements

### Frontend

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