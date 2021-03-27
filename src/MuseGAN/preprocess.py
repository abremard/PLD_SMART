import os
import matplotlib.pyplot as plt
import numpy as np
import types

from utils.loaders import load_music

# ---- 1 song 1 track ~20 measures ~80 beats 128 possible pitches (C1-G9)
# TODO: conversion function
# 1) if we keep 2 measures like in the original model, we would keep only data[:192]
# 2) reshape it to (1, 2, 96, 128) (last dimension must have values -1 or 1 only)
# 3) combine with other 4 tracks and output a tensor of shape (1, 2, 96, 128, 5)

print("OLD VERSION")
# run params
SECTION = 'compose'
RUN_ID = '001'
DATA_NAME = 'chorales'
FILENAME = 'Jsb16thSeparated.npz'
RUN_FOLDER = 'run/{}/'.format(SECTION)
RUN_FOLDER += '_'.join([RUN_ID, DATA_NAME])

BATCH_SIZE = 64
n_bars = 2
n_steps_per_bar = 16
n_pitches = 84
n_tracks = 4

data_binary, data_ints, raw_data = load_music(DATA_NAME, FILENAME, n_bars, n_steps_per_bar)
print(data_binary.shape)
print(data_ints.shape)
print(raw_data.shape)
print(raw_data[0].shape)

print("NEW VERSION")

file = os.path.join("./data", "chorales", "b97c529ab9ef783a849b896816001748.npz")

with np.load(file, encoding='bytes', allow_pickle = True) as f:
    data = f['pianoroll_0_csc_data']
    print('pianoroll 0 csc data')
    print(data.shape)
    print(data[:64])