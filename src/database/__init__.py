"""
Scripts for editing the Firebase database
"""
import os
import sys
from database.metadata_processing import *
from database.firestore import *
import re


def format_file_name(file_name: str) -> str:
    file_name = file_name[:-4]  # remove extension first -> todo check if there are .midi files instead of .mid

    # print(f"--- file name: {file_name}")
    if len(re.findall('\\.', file_name)) > 0:
        # print(f"WARNING: using format_string on a file name containing dots! ({file_name})", file=sys.stderr)
        # print(f"before sub: {file_name}")
        formatted_name = re.sub(".mid", "", file_name)
        # print(f"after sub .mid: {formatted_name}")
        formatted_name = re.sub("\\.", "_", formatted_name)
        # print(f"after sub .: {formatted_name}")
        formatted_name = format_string(formatted_name)
        # print(f"after formatting: {formatted_name}")
    else:
        formatted_name = format_string(str(file_name).split('.')[0])

    formatted_name = re.sub("-", "_", formatted_name)
    return f"{formatted_name}.mid"


def get_formatted_file_path(file_path: str) -> str:
    """
    Only format the file name, then return the whole path with the new file name
    Args:
        file_path: The path to format

    Returns: The formatted file path

    """

    # print(f"input path: {file_path}")
    path_to_file_dir = os.path.abspath(os.path.dirname(file_path))
    file_name = os.path.basename(file_path)

    formatted_name = format_file_name(file_name)
    return os.path.join(path_to_file_dir, formatted_name)


def rename_files_in_dir(directory_path: str, verbose=False):
    directory = os.path.dirname(directory_path)

    for dirpath, subdirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.normpath(os.path.join(dirpath, filename))
            new_file_path = get_formatted_file_path(file_path)
            if verbose:
                print(f">> renaming {file_path} --->>> {new_file_path}")
            os.replace(file_path, new_file_path)  # rename the file   # todo uncomment when ok


def get_track_instrument(filename: str) -> str:

    instruments = ("guitar", "drums", "piano", "bass", "strings")
    for instrument in instruments:
        if len(re.findall(instrument, filename)) > 0:
            return instrument


# main method linking all the important processing stuff
def process_files_from_dir(directory_path: str):
    init_firebase_connexion()       # todo uncomment
    init_spotify_connexion()        # todo uncomment

    # reset_database()  # todo comment when updating

    directory = os.path.abspath(os.path.dirname(directory_path))

    # first, rename files to a correct format
    print(f">>> Renaming files in {directory}")
    rename_files_in_dir(directory_path)

    # file by file, upload its metadata & the file itself
    for dirpath, subdirs, files in os.walk(directory):

        # get metadata about the file
        artist = os.path.basename(dirpath)
        formatted_artist = format_string(artist)
        genre = get_artist_genre(artist)
        print(f"----- Current dir: artist {artist} and genre {genre}, {len(files)} files to process.")

        for filename in files:
            # get track instrument
            instrument = get_track_instrument(filename)
            print(f"> Current file: {filename}, instrument: {instrument}")

            # -- upload midi to firebase
            file_path = os.path.join(dirpath, filename)
            firebase_path_from_midi_dir = f"{formatted_artist}/{filename}"
            # print(f"Uploading file from {file_path} to {firebase_path_from_midi_dir}")
            upload_midi_file(local_file_path=file_path, firebase_file_path_from_midi_dir=firebase_path_from_midi_dir)   # todo uncomment when ok

            # -- update database
            add_entry(firebase_path_from_midi_dir, genre, artist, instrument)


def main():

    if len(sys.argv) > 1:
        input_path = sys.argv[1]
        if input_path[-1] != "/":   # maybe no longer needed?
            input_path += "/"

        dirname = os.path.dirname(__file__)
        dir = os.path.join(dirname, input_path)

        process_files_from_dir(dir)

    else:
        raise Exception("No input provided: please provide the path to the directory you wish to process")


if __name__ == '__main__':
    main()
