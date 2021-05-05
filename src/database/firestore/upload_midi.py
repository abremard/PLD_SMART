"""
Function for uploading MIDI files in Firebase
"""

import firebase_admin
from firebase_admin import credentials, firestore, storage
import sys
import os
from src.database.firestore.utils_firestore import *


def upload_midi_file(local_file_path: str, firebase_file_path_from_midi_dir: str, verbose=False):
    """
    Uploads the given MIDI file to the Firebase storage

    Args:
        local_file_path: The path to the file to upload
        firebase_file_path_from_midi_dir: The path where the file should be uploaded to in Firebase
        verbose: Set this to True for more prints

    Returns: void

    """

    db = firestore.client()
    bucket = storage.bucket()  # ref to Firebase Storage

    # output file (path & name in Firebase Storage)
    blob = bucket.blob(f'MIDI/{firebase_file_path_from_midi_dir}')

    with open(local_file_path, 'rb') as local_file:
        blob.upload_from_file(local_file)

        if verbose:
            print(f"file {local_file_path} uploaded", file=sys.stderr)


# --- tests
if __name__ == "__main__":

    init_firebase_connexion()
    # test
    test_firebase_file_name = "Gipsy_kings/DELETE_ME.mid"
    local_path = '../test_data/Gipsy Kings/Baila Me.mid_drums.mid'

    dirname = os.path.dirname(__file__)
    test_local_path = os.path.join(dirname, local_path)

    upload_midi_file(test_local_path, test_firebase_file_name)
