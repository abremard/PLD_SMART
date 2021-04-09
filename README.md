# PLD_SMART

## Description

## Frontend

## Backend

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