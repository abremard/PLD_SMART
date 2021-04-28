import os

from mido import MidiFile


def _find_files(filename, search_path):
   result = []

   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result

def _sort_midi_tracks(midiName):
    mid = MidiFile(midiName, clip=True)
    bassNumber = 0
    stringsNumber = 0
    drumsNumber = 0
    guitarNumber = 0
    pianoNumber = 0

    for track in mid.tracks:
        if ("BASS" in track):
            newMid = MidiFile()
            newMid.tracks.append(track)
            if not _find_files(midiName + '_bass.mid', '.'):
                newMid.save(midiName + '_bass.mid')
            else:
                bassNumber += 1
                newMid.save(midiName + '_bass.mid' + bassNumber + '.mid')
        elif ("STRINGS" in track):
            newMid = MidiFile()
            newMid.tracks.append(track)
            if not _find_files(midiName + '_strings.mid', '.'):
                newMid.save(midiName + '_strings.mid')
            else:
                stringsNumber += 1
                newMid.save(midiName + '_strings_' + stringsNumber + '.mid')
        elif ("DRUMS" in track):
            newMid = MidiFile()
            newMid.tracks.append(track)
            if not _find_files(midiName + '_drums.mid', '.'):
                newMid.save(midiName + '_drums.mid')
            else:
                drumsNumber += 1
                newMid.save(midiName + '_drums_' + drumsNumber + '.mid')
        elif ("GUITAR" in track):
            newMid = MidiFile()
            newMid.tracks.append(track)
            if not _find_files(midiName + '_guitar.mid', '.'):
                newMid.save(midiName + '_guitar.mid')
            else:
                guitarNumber += 1
                newMid.save(midiName + '_guitar_' + guitarNumber + '.mid')
        elif ("PIANO" in track):
            newMid = MidiFile()
            newMid.tracks.append(track)
            if not _find_files(midiName + '_piano.mid', '.'):
                newMid.save(midiName + '_piano.mid')
            else:
                pianoNumber += 1
                newMid.save(midiName + '_piano_' + pianoNumber + '.mid')


def sort_midi_files(directoryPath):
    for mainDirectory in os.walk(directoryPath):
        for directory in mainDirectory:
            for filename in directory:
                if filename.endswith(".mid"):
                    _sort_midi_tracks(filename)
                    continue
                else:
                    continue