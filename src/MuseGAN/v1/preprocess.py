""" Preprocess LPD data for training
"""

from pathlib import Path
parent = Path(__file__).resolve().parent
srcPath = str(parent).replace("\\", "\\\\")
import sys
sys.path.insert(0, srcPath)

import os
import matplotlib.pyplot as plt
import numpy as np
import types
import pypianoroll
import pprint
import math
import os
import pandas as pd

from wrappers import pypianoroll as ppr

pp = pprint.PrettyPrinter(indent=4)

# ******* LPD Dataset *******

def fetchFileNames(root="./data/lpd_5_cleansed", output='paths.csv'):
    """ Run once to get array containing paths to .npz files

    Args:
        root (str, optional): data root directory. Defaults to "./data/lpd_5_cleansed".
        output (str, optional): output file path, must be .csv. Defaults to 'paths.csv'.
    """    
    pathArray = []

    for root, dirs, files in os.walk(root):
        for file in files:
            if file.endswith(".npz"):
                pathArray.append(os.path.join(root, file))

    pathDF = pd.DataFrame(pathArray)
    pathDF.to_csv(output)

def preprocess(inputPaths, n_songs, n_bars, n_steps_per_bar, n_pitches, n_instruments, bars_offset):
    """ Preprocess npz file and reshape as numpy 5-dimensional array for training.
        ------ (n_songs, n_bars, n_steps_per_bar, n_pitches, n_instruments) -----
        Each song must contain 24 measures = 96 beats
        Each beat have 128 possible pitches (C1-G9)
        Beat resolution is 24

    Args:
        inputPaths (str): path of csv file containing all .npz file paths 
        n_songs (int): number of songs to include in batch
        n_bars (int): number of bars to keep per song
        n_steps_per_bar (int): bar resolution
        n_pitches (int): pitch resolution
        n_instruments (int): number of instruments
    """    

    pathDF = pd.read_csv(inputPaths)

    multitrack = np.zeros((n_songs, n_bars, n_steps_per_bar, n_pitches, n_instruments))

    for index, row in pathDF.iterrows():
        
        tmpArray = np.zeros((n_instruments, n_bars, n_steps_per_bar, n_pitches))
        
        for item in range(n_instruments):
            
            track = ppr.load(row['Path']).tracks[item]
            pianoroll = track.pianoroll
            
            if ppr.load(row['Path']).tracks[item].pianoroll.shape[0] == 0:
                pianoroll = np.zeros((n_bars*n_steps_per_bar, n_pitches))

            # map velocity to -1 and 1
            pianoroll = np.ceil(pianoroll / 127).astype(int)
            pianoroll = np.where(pianoroll==0, -1, pianoroll)   
            # quotient
            n_init_bars = pianoroll.shape[0] // n_steps_per_bar
            # remove remainder
            floor = n_init_bars*n_steps_per_bar
            # reshape
            newpianoroll = pianoroll[:floor].reshape(n_init_bars, n_steps_per_bar, n_pitches)

            slicedpianoroll = newpianoroll[bars_offset:n_bars, :, :]
                            
            tmpArray[item] = slicedpianoroll
            
        # transpose
        tmpArray = np.swapaxes(tmpArray, 0, 1)
        tmpArray = np.swapaxes(tmpArray, 1, 2)
        tmpArray = np.swapaxes(tmpArray, 2, 3)
                        
        multitrack[index] = tmpArray
        if index == n_songs - 1:
            break

    return multitrack


if __name__ == "__main__":
    """ 
        for 100 songs ~ 3GB of RAM 
        --> find a solution to train using buffer
        check out keras fit_generator at https://www.pyimagesearch.com/2018/12/24/how-to-use-keras-fit-and-fit_generator-a-hands-on-tutorial/
    """    
    
    n_songs = 10
    n_bars = 24
    n_steps_per_bar = 96
    n_pitches = 128
    n_instruments = 5
    bars_offset = 12
    
    multitrack = preprocess(
                inputPaths='paths.csv',
                n_songs=n_songs,
                n_bars=n_bars,
                n_steps_per_bar=n_steps_per_bar,
                n_pitches=n_pitches,
                n_instruments=n_instruments,
                bars_offset=bars_offset)

# ******* JSB chorales *******

# from utils.loaders import load_music

# # run params
# SECTION = 'compose'
# RUN_ID = '001'
# DATA_NAME = 'chorales'
# FILENAME = 'Jsb16thSeparated.npz'
# RUN_FOLDER = 'run/{}/'.format(SECTION)
# RUN_FOLDER += '_'.join([RUN_ID, DATA_NAME])

# BATCH_SIZE = 64
# n_bars = 2
# n_steps_per_bar = 16
# n_pitches = 84
# n_tracks = 4

# data_binary, data_ints, raw_data = load_music(DATA_NAME, FILENAME, n_bars, n_steps_per_bar)
# print(data_binary.shape)
# print(data_ints.shape)
# print(raw_data.shape)
# print(raw_data[0].shape)