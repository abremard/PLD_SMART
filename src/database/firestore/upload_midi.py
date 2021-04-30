"""
Script for uploading MIDI files in Firebase

TODO:
    - bulk read a folder, recursively or not, then preprocess metadata & file
    names, then upload them
    - add an upload & transfer limit check, don't upload if there's no more
     credit (or not much)
"""

import firebase_admin
from firebase_admin import credentials, firestore, storage
import sys
import os
from src.database.firestore.utils_firestore import *    # initializes firebase connexion


def upload_midi_file(local_file_path: str, firebase_file_name: str, verbose=False):

    db = firestore.client()
    bucket = storage.bucket()  # ref to Firebase Storage

    # output file (path & name in Firebase Storage)
    blob = bucket.blob(f'MIDI/{firebase_file_name}')

    with open(local_file_path, 'rb') as local_file:
        blob.upload_from_file(local_file)

        if verbose:
            print(f"file {local_file_path} uploaded", file=sys.stderr)


if __name__ == "__main__":

    init_firebase_connexion()
    # test
    test_firebase_file_name = "freedom_dive.mid"

    dirname = os.path.dirname(__file__)
    test_local_path = os.path.join(dirname, '../test_data/Freedom Dive.mid')

    upload_midi_file(test_local_path, test_firebase_file_name)
