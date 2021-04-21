import __init__

import os
import matplotlib.pyplot as plt
import numpy as np
import types

from models.MuseGAN import MuseGAN
from utils.loaders import load_music

from music21 import midi
from music21 import note, stream, duration

from tensorflow.keras.models import load_model

import base64
from mailjet_rest import Client

n_songs = 500
n_bars = 6
n_steps_per_bar = 96
n_pitches = 128
n_tracks = 5
bars_offset = 8

BATCH_SIZE = 64
SECTION = 'compose'
RUN_ID = '002'
DATA_NAME = 'lpd'
RUN_FOLDER = 'src/algo/MuseGAN/v0/run/{}/'.format(SECTION)
RUN_FOLDER += '_'.join([RUN_ID, DATA_NAME])

if not os.path.exists(RUN_FOLDER):
    os.mkdir(RUN_FOLDER)
    os.mkdir(os.path.join(RUN_FOLDER, 'viz'))
    os.mkdir(os.path.join(RUN_FOLDER, 'images'))
    os.mkdir(os.path.join(RUN_FOLDER, 'weights'))
    os.mkdir(os.path.join(RUN_FOLDER, 'samples'))

shape = (n_bars, n_steps_per_bar, n_pitches, n_tracks)

gan = MuseGAN(input_dim = shape
        , critic_learning_rate = 0.001
        , generator_learning_rate = 0.001
        , optimiser = 'adam'
        , grad_weight = 10
        , z_dim = n_bars*n_steps_per_bar
        , batch_size = BATCH_SIZE
        , n_tracks = n_tracks
        , n_bars = n_bars
        , n_steps_per_bar = n_steps_per_bar
        , n_pitches = n_pitches
        )

gan.load_weights(RUN_FOLDER, None)

gan.generator.summary()

gan.critic.summary()

for i in range(10):
    chords_noise = np.random.normal(0, 1, (1, gan.z_dim))
    style_noise = np.random.normal(0, 1, (1, gan.z_dim))
    melody_noise = np.random.normal(0, 1, (1, gan.n_tracks, gan.z_dim))
    groove_noise = np.random.normal(0, 1, (1, gan.n_tracks, gan.z_dim))

    gen_scores = gan.generator.predict([chords_noise, style_noise, melody_noise, groove_noise])

    # np.argmax(gen_scores[0,0,0:4,:,3], axis = 1)

    filename = 'example'+str(i)
    gan.notes_to_midi(RUN_FOLDER, gen_scores, filename)

# gan.draw_score(gen_scores, 0)

# chords_noise_2 = 5 * np.ones((1, gan.z_dim))

# chords_scores = gan.generator.predict([chords_noise_2, style_noise, melody_noise, groove_noise])

# filename = 'changing_chords'
# gan.notes_to_midi(RUN_FOLDER, chords_scores, filename)
# chords_score = converter.parse(os.path.join(RUN_FOLDER, 'samples/{}.midi'.format(filename)))
# print('original')
# gen_score.show()
# print('chords noise changed')
# chords_score.show()

# style_noise_2 = 5 * np.ones((1, gan.z_dim))

# style_scores = gan.generator.predict([chords_noise, style_noise_2, melody_noise, groove_noise])

# filename = 'changing_style'
# gan.notes_to_midi(RUN_FOLDER, style_scores, filename)
# style_score = converter.parse(os.path.join(RUN_FOLDER, 'samples/{}.midi'.format(filename)))
# print('original')
# gen_score.show()
# print('style noise changed')
# style_score.show()

# melody_noise_2 = np.copy(melody_noise)
# melody_noise_2[0,0,:] = 5 * np.ones(gan.z_dim) 

# melody_scores = gan.generator.predict([chords_noise, style_noise, melody_noise_2, groove_noise])

# filename = 'changing_melody'
# gan.notes_to_midi(RUN_FOLDER, melody_scores, filename)
# melody_score = converter.parse(os.path.join(RUN_FOLDER, 'samples/{}.midi'.format(filename)))
# print('original')
# gen_score.show()
# print('melody noise changed')
# melody_score.show()

# groove_noise_2 = np.copy(groove_noise)
# groove_noise_2[0,3,:] = 5 * np.ones(gan.z_dim)

# groove_scores = gan.generator.predict([chords_noise, style_noise, melody_noise, groove_noise_2])

# filename = 'changing_groove'
# gan.notes_to_midi(RUN_FOLDER, groove_scores, filename)
# groove_score = converter.parse(os.path.join(RUN_FOLDER, 'samples/{}.midi'.format(filename)))
# print('original')
# gen_score.show()
# print('groove noise changed')
# groove_score.show()