import sys
sys.path.insert(0,'PLD_SMART/src')

import os
import matplotlib.pyplot as plt
import numpy as np
import types

from algo.MuseGAN.v0.models.MuseGAN import MuseGAN
from utils.loaders import load_music

from music21 import midi
from music21 import note, stream, duration

from tensorflow.keras.models import load_model

import base64
import mido

def generate(
    run_id = "001",
    chords = None,
    style = None,
    melody_drum = None,
    melody_piano = None,
    melody_guitar = None,
    melody_bass = None,
    melody_strings = None,
    groove_drum = None,
    groove_piano = None,
    groove_guitar = None,
    groove_bass = None,
    groove_strings = None):

    n_songs = 10
    n_bars = 2
    n_steps_per_bar = 96
    n_pitches = 128
    n_tracks = 5
    bars_offset = 12

    mode =  'build' # ' 'load' #
    BATCH_SIZE = 64
    SECTION = 'compose'
    RUN_ID = run_id
    DATA_NAME = 'lpd'
    RUN_FOLDER = '/content/drive/My Drive/SMART/MuseGAN/run/compose/'
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

    # TODO : process input params

    chords_noise = np.random.normal(0, 1, (1, gan.z_dim))
    style_noise = np.random.normal(0, 1, (1, gan.z_dim))
    melody_noise = np.random.normal(0, 1, (1, gan.n_tracks, gan.z_dim))
    groove_noise = np.random.normal(0, 1, (1, gan.n_tracks, gan.z_dim))
    
    if chords is not None :
        chords_noise = chords * np.ones((1, gan.z_dim))
    if style is not None :
        style_noise = style * np.ones((1, gan.z_dim))
    if melody_drum is not None:
        melody_noise[0,0,:] = melody_drum * np.ones(gan.z_dim)
    if melody_piano is not None:
        melody_noise[0,1,:] = melody_piano * np.ones(gan.z_dim) 
    if melody_guitar is not None:
        melody_noise[0,2,:] = melody_guitar * np.ones(gan.z_dim)
    if melody_bass is not None:
        melody_noise[0,3,:] = melody_bass * np.ones(gan.z_dim) 
    if melody_strings is not None:
        melody_noise[0,4,:] = melody_strings * np.ones(gan.z_dim) 
    if groove_drum is not None:
        groove_noise[0,0,:] = groove_drum * np.ones(gan.z_dim)
    if groove_piano is not None:
        groove_noise[0,1,:] = groove_piano * np.ones(gan.z_dim) 
    if groove_guitar is not None:
        groove_noise[0,2,:] = groove_guitar * np.ones(gan.z_dim)
    if groove_bass is not None:
        groove_noise[0,3,:] = groove_bass * np.ones(gan.z_dim) 
    if groove_strings is not None:
        groove_noise[0,4,:] = groove_strings * np.ones(gan.z_dim) 

    gen_scores = gan.generator.predict([chords_noise, style_noise, melody_noise, groove_noise])

    np.argmax(gen_scores[0,0,0:4,:,3], axis = 1)

    gen_scores[0,0,0:4,60,3] = 0.02347812

    filename = 'example'
    gan.notes_to_midi(RUN_FOLDER, gen_scores, filename)
    gan.draw_score(gen_scores, 0)

    chords_noise_2 = 5 * np.ones((1, gan.z_dim))

    chords_scores = gan.generator.predict([chords_noise_2, style_noise, melody_noise, groove_noise])

    filename = 'changing_chords'
    gan.notes_to_midi(RUN_FOLDER, chords_scores, filename)
    # chords_score = converter.parse(os.path.join(RUN_FOLDER, 'samples/{}.midi'.format(filename)))
    # print('original')
    # gen_score.show()
    # print('chords noise changed')
    # chords_score.show()

    style_noise_2 = 5 * np.ones((1, gan.z_dim))

    style_scores = gan.generator.predict([chords_noise, style_noise_2, melody_noise, groove_noise])

    filename = 'changing_style'
    gan.notes_to_midi(RUN_FOLDER, style_scores, filename)
    # style_score = converter.parse(os.path.join(RUN_FOLDER, 'samples/{}.midi'.format(filename)))
    # print('original')
    # gen_score.show()
    # print('style noise changed')
    # style_score.show()

    melody_noise_2 = np.copy(melody_noise)
    melody_noise_2[0,0,:] = 5 * np.ones(gan.z_dim) 

    melody_scores = gan.generator.predict([chords_noise, style_noise, melody_noise_2, groove_noise])

    filename = 'changing_melody'
    gan.notes_to_midi(RUN_FOLDER, melody_scores, filename)
    # melody_score = converter.parse(os.path.join(RUN_FOLDER, 'samples/{}.midi'.format(filename)))
    # print('original')
    # gen_score.show()
    # print('melody noise changed')
    # melody_score.show()

    groove_noise_2 = np.copy(groove_noise)
    groove_noise_2[0,3,:] = 5 * np.ones(gan.z_dim)

    groove_scores = gan.generator.predict([chords_noise, style_noise, melody_noise, groove_noise_2])

    filename = 'changing_groove'
    gan.notes_to_midi(RUN_FOLDER, groove_scores, filename)
    # groove_score = converter.parse(os.path.join(RUN_FOLDER, 'samples/{}.midi'.format(filename)))
    # print('original')
    # gen_score.show()
    # print('groove noise changed')
    # groove_score.show()

    output_file_path = RUN_FOLDER + '/samples/example.midi'

    change_instruments(output_file_path)
    
    return output_file_path


def change_instruments(file_path: str):

    mid = mido.MidiFile(file_path)
    # print(mid.type, mid.length, mid.ticks_per_beat)

    # remove old program_change messages
    for track in mid.tracks:
        print(track.name)
        for msg in track:
            if msg.type == "program_change":
                # print(f"Program change msg in original file: {msg}")
                track.remove(msg)

    """
    bass 35
    drums 118
    guitar 24
    strings 41
    piano 0
    """
    instruments = (35, 118, 24, 41, 0)

    # add new program_change messages
    for i_track, track in enumerate(mid.tracks):
        # print(f"track: {track}")

        # track 0 will use channel 0 only, track 1 channel 1 only, ...
        track.insert(0, mido.Message(type="program_change", channel=i_track, program=instruments[i_track]))

        for msg in track:
            if msg.type in ("note_on", "note_off"):
                msg.channel = i_track

    # check new program_change messages
    # for i, track in enumerate(mid.tracks):
    #     for msg in track:
    #         # print(msg)
    #         if msg.type == "program_change":
    #             print(f"track no {i} : msg: {msg}")
    #             # track.remove(msg)
    #
    # print()

    mid.save(file_path)