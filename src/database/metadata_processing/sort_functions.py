import os

from mido import MidiFile


def _find_files(filename, searchPath):
    result = []
    print("search path = " + searchPath)
    print("filename = " + filename)

    for root, dir, files in os.walk(searchPath):
        print("files = " + str(files))
        if filename in files:
            result.append(os.path.join(root, filename))
        return result


def _sort_midi_tracks(midiName, filePath, searchPath):
    mid = MidiFile(filePath, clip=True)
    bassNumber = 0
    stringsNumber = 0
    drumsNumber = 0
    guitarNumber = 0
    pianoNumber = 0

    for track in mid.tracks:
        if "bass" in str(track) or "BASS" in str(track):
            newMid = MidiFile()
            newMid.tracks.append(track)
            if not _find_files(midiName + '_bass.mid', searchPath):
                newMid.save(filePath + '_bass.mid')
            else:
                bassNumber += 1
                newMid.save(filePath + '_bass.mid' + str(bassNumber) + '.mid')
        elif "strings" in str(track) or "STRINGS" in str(track):
            newMid = MidiFile()
            newMid.tracks.append(track)
            if not _find_files(midiName + '_strings.mid', searchPath):
                newMid.save(filePath + '_strings.mid')
            else:
                stringsNumber += 1
                newMid.save(filePath + '_strings_' + str(stringsNumber) + '.mid')
        elif "drums" in str(track) or "DRUMS" in str(track):
            newMid = MidiFile()
            newMid.tracks.append(track)
            if not _find_files(midiName + '_drums.mid', searchPath):
                newMid.save(filePath + '_drums.mid')
            else:
                drumsNumber += 1
                newMid.save(filePath + '_drums_' + str(drumsNumber) + '.mid')
        elif "guitar" in str(track) or "GUITAR" in str(track):
            newMid = MidiFile()
            newMid.tracks.append(track)
            if not _find_files(midiName + '_guitar.mid', searchPath):
                newMid.save(filePath + '_guitar.mid')
            else:
                guitarNumber += 1
                newMid.save(filePath + '_guitar_' + str(guitarNumber) + '.mid')
        elif "piano" in str(track) or "PIANO" in str(track):
            newMid = MidiFile()
            newMid.tracks.append(track)
            if not _find_files(midiName + '_piano.mid', searchPath):
                newMid.save(filePath + '_piano.mid')
            else:
                pianoNumber += 1
                newMid.save(filePath + '_piano_' + str(pianoNumber) + '.mid')


def sort_midi_files(directoryPath):
    for subdir, dirs, files in os.walk(directoryPath):
        for fileName in files:
            if fileName.endswith(".mid"):
                _sort_midi_tracks(fileName, os.path.join(subdir, fileName),
                                  os.path.dirname(os.path.join(subdir, fileName)))
            os.remove(os.path.join(subdir, fileName))
