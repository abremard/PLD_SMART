import os
import pickle
import numpy
from music21 import note, chord

from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from tensorflow.keras.utils import plot_model

from algo.LSTM.models.RNNAttention import get_distinct, create_lookups, prepare_sequences, get_music_list, create_network

def train(section, run_id, music_name):
    """
        PARAMS
        section = 'compose'
        run_id = "001"
        music_name = 'acdc'
    """
    run_folder = '/content/drive/My Drive/SMART/LSTM/run/'
    run_folder += '_'.join([run_id, music_name])

    store_folder = os.path.join(run_folder, 'store')
    data_folder = os.path.join('/content/drive/My Drive/SMART/LSTM/data', music_name)

    if not os.path.exists(run_folder):
        os.mkdir(run_folder)
        os.mkdir(os.path.join(run_folder, 'store'))
        os.mkdir(os.path.join(run_folder, 'output'))
        os.mkdir(os.path.join(run_folder, 'weights'))
        os.mkdir(os.path.join(run_folder, 'viz'))
        


    mode = 'build' # 'load' # 

    # data params
    intervals = range(1)
    seq_len = 32

    # model params
    embed_size = 100
    rnn_units = 256
    use_attention = True

    if mode == 'build':
        
        music_list, parser = get_music_list(data_folder)
        print(len(music_list), 'files in total')

        notes = []
        durations = []

        for i, file in enumerate(music_list):
            print(i+1, "Parsing %s" % file)
            original_score = parser.parse(file).chordify()
            
            for interval in intervals:

                score = original_score.transpose(interval)
                
                notes.extend(['START'] * seq_len)
                durations.extend([0]* seq_len)

                for element in score.flat:
                    if isinstance(element, note.Note):
                        if element.isRest:
                            notes.append(str(element.name))
                            durations.append(element.duration.quarterLength)
                        else:
                            notes.append(str(element.nameWithOctave))
                            durations.append(element.duration.quarterLength)

                    if isinstance(element, chord.Chord):
                        notes.append('.'.join(n.nameWithOctave for n in element.pitches))
                        durations.append(element.duration.quarterLength)
                print(notes)
                print(durations)

        with open(os.path.join(store_folder, 'notes'), 'wb') as f:
            pickle.dump(notes, f) #['G2', 'D3', 'B3', 'A3', 'B3', 'D3', 'B3', 'D3', 'G2',...]
        with open(os.path.join(store_folder, 'durations'), 'wb') as f:
            pickle.dump(durations, f) 
    else:
        with open(os.path.join(store_folder, 'notes'), 'rb') as f:
            notes = pickle.load(f) #['G2', 'D3', 'B3', 'A3', 'B3', 'D3', 'B3', 'D3', 'G2',...]
        with open(os.path.join(store_folder, 'durations'), 'rb') as f:
            durations = pickle.load(f) 

            
    # get the distinct sets of notes and durations
    note_names, n_notes = get_distinct(notes)
    duration_names, n_durations = get_distinct(durations)
    distincts = [note_names, n_notes, duration_names, n_durations]

    with open(os.path.join(store_folder, 'distincts'), 'wb') as f:
        pickle.dump(distincts, f)

    # make the lookup dictionaries for notes and dictionaries and save
    note_to_int, int_to_note = create_lookups(note_names)
    duration_to_int, int_to_duration = create_lookups(duration_names)
    lookups = [note_to_int, int_to_note, duration_to_int, int_to_duration]

    with open(os.path.join(store_folder, 'lookups'), 'wb') as f:
        pickle.dump(lookups, f)
        
    print('\nnote_to_int')
    note_to_int

    print('\nduration_to_int')
    duration_to_int

    network_input, network_output = prepare_sequences(notes, durations, lookups, distincts, seq_len)

    print('pitch input')
    print(network_input[0][0])
    print('duration input')
    print(network_input[1][0])
    print('pitch output')
    print(network_output[0][0])
    print('duration output')
    print(network_output[1][0])

    model, att_model = create_network(n_notes, n_durations, embed_size, rnn_units, use_attention)
    model.summary()

    #Currently errors in TF2.2
    #plot_model(model, to_file=os.path.join(run_folder ,'viz/model.png'), show_shapes = True, show_layer_names = True)

    weights_folder = os.path.join(run_folder, 'weights')
    # model.load_weights(os.path.join(weights_folder, "weights.h5"))

    weights_folder = os.path.join(run_folder, 'weights')

    checkpoint1 = ModelCheckpoint(
        os.path.join(weights_folder, "weights-improvement-{epoch:02d}-{loss:.4f}-bigger.h5"),
        monitor='loss',
        verbose=0,
        save_best_only=True,
        mode='min'
    )

    checkpoint2 = ModelCheckpoint(
        os.path.join(weights_folder, "weights.h5"),
        monitor='loss',
        verbose=0,
        save_best_only=True,
        mode='min'
    )

    early_stopping = EarlyStopping(
        monitor='loss'
        , restore_best_weights=True
        , patience = 10
    )


    callbacks_list = [
        checkpoint1
        , checkpoint2
        , early_stopping
    ]

    model.save_weights(os.path.join(weights_folder, "weights.h5"))
    model.fit(network_input, network_output
            , epochs=50, batch_size=64
            , validation_split = 0.2
            , callbacks=callbacks_list
            , shuffle=True
            )
