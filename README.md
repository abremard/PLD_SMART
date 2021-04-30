# PLD_SMART

## Description

## Frontend

## Backend

## Database

### Firestore
Requirements to use Python scripts to edit the Firestore database (tested on Python 3.8):
 - copy the `cred.json` I sent you into `src/database/firestore/` (:warning: : NEVER commit this file on VCS, it contains credentials giving write access to the DB)
 - install the required modules : (requires pip to work):
 ```shell script
> pip install firebase_admin unidecode
```

### Metadata processing
Requirements to use Python scripts wih Spotify's API (tested on Python 3.8):
 - copy the `spotify_credentials.txt` I sent you into `src/database/metadata_processing/` (:warning: : NEVER commit this file on VCS, it contains out unique credentials)
 - install the required modules : (requires pip to work):
 ```shell script
> pip install spotipy mido
```
:warning: `python-Levenshtein` requires Microsoft Visual C++ 14.0


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