# import pypianoroll


# path = 'data/output.npz'
# multitrack = pypianoroll.read(path="HighwayToHell.mid")

# pypianoroll.save(path=path, multitrack=multitrack)

from numpy import load

data = load('data/output.npz')
lst = data.files
for item in lst:
    print(item)
    print(data[item])

# import numpy as np
# # from pypianoroll import Multitrack
# import pypianoroll as ppr

# # multitrack = pypianoroll.load('data.npz')

# # pypianoroll.write('test.mid', multitrack)

# # # from pypianoroll import Multitrack

# # # Parameters
# # FILENAMES = ['test.mid'] # The input MIDI filenames
# # RESULT_FILENAME= 'data/output.npz' # The resulting filename
# # N_TRACKS = 1
# # BEAT_RESOLUTION = 84 # The beat resolution

# # # Initialize an empty list to collect the results
# # results = []

# # # Iterate through all the MIDI files
# # for filename in FILENAMES:
    
# #     # Parse the MIDI file into multitrack pianoroll
# #     try:
# #         multitrack  = pypianoroll.read('test.mid')
# #         # multitrack  = Multitrack(filename, beat_resolution=BEAT_RESOLUTION)
# #     except:
# #         continue
    
# #     # Pad to multtple
# #     multitrack.pad_to_multiple(4 * BEAT_RESOLUTION)

# #     # Binarize the pianoroll
# #     multitrack.binarize()

# #     # Sort the tracks according to program number
# #     multitrack.tracks.sort(key=lambda x: x.program)

# #     # Bring the drum track to the first track
# #     multitrack.tracks.sort(key=lambda x: ~x.is_drum)

# #     # Get the stacked pianoroll
# #     pianoroll = multitrack[0].pianoroll
    
# #     # Check length
# #     if pianoroll.shape[0] < 4 * 4 * BEAT_RESOLUTION:
# #         continue

# #     # Keep only the mid-range pitches
# #     pianoroll = pianoroll[:, 24:108]

# #     # Reshape and get the phrase pianorolls
# #     pianoroll = pianoroll.reshape(-1, 4 * BEAT_RESOLUTION, 84, N_TRACKS)
# #     results.append(np.concatenate(
# #         [pianoroll[:-3], pianoroll[1:-2], pianoroll[2:-1], pianoroll[3:]], 1))

# # result = np.concatenate(results, 0)
# # # NOTE: You might want to shuffle the training data here
# # np.savez_compressed(
# #     RESULT_FILENAME, nonzero=np.array(result.nonzero()),
# #     shape=result.shape)

# # multitrack = pypianoroll.load('data/output.npz')

# # print(multitrack)

# path = "data.npz"
# n_songs = 1
# n_bars = 4
# n_steps_per_bar = 96
# n_pitches = 128
# n_instruments = 5
# bars_offset = 2

# multitrack = np.zeros((n_songs, n_bars, n_steps_per_bar, n_pitches, n_instruments))

# for item in range(n_instruments):

#     tmpArray = np.zeros((n_instruments, n_bars, n_steps_per_bar, n_pitches))

#     track = ppr.load(path).tracks[item]
#     pianoroll = track.pianoroll
    
#     if ppr.load(path).tracks[item].pianoroll.shape[0] == 0:
#         pianoroll = np.zeros(((n_bars+bars_offset)*n_steps_per_bar, n_pitches))


#     # map velocity to -1 and 1
#     pianoroll = np.ceil(pianoroll / 127).astype(int)
#     pianoroll = np.where(pianoroll==0, -1, pianoroll)   
#     # quotient
#     n_init_bars = pianoroll.shape[0] // n_steps_per_bar
#     # remove remainder
#     floor = n_init_bars*n_steps_per_bar
#     # reshape

#     newpianoroll = pianoroll[:floor].reshape(n_init_bars, n_steps_per_bar, n_pitches)

#     slicedpianoroll = newpianoroll[bars_offset:bars_offset+n_bars, :, :]
                    
#     tmpArray[item] = slicedpianoroll
    
# # transpose
# tmpArray = np.swapaxes(tmpArray, 0, 1)
# tmpArray = np.swapaxes(tmpArray, 1, 2)
# tmpArray = np.swapaxes(tmpArray, 2, 3)
                
# multitrack[0] = tmpArray

# np.save('data/output.npy', multitrack)