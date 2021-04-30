"""
Script for uploading MIDI files in Firebase

TODO:
    - bulk read a folder, recursively or not, then preprocess metadata & file
    names, then upload them
    - firestore: maybe add a Songs collection to access metadata for a give file
    - add an upload & transfer limit check, don't upload if there's no more
     credit (or not much)
"""

import firebase_admin
from firebase_admin import credentials, firestore, storage
import sys

# ----------- Initialize Firebase connexion
# Use a service account
cred = credentials.Certificate("./cred.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'ilolio.appspot.com'       # default bucket, maybe change for a custom bucket later
})

db = firestore.client()
bucket = storage.bucket()       # ref to Firebase Storage


def upload_midi_file(local_file_path: str, firebase_file_name: str, verbose=False):

    # output file (path & name in Firebase Storage)
    blob = bucket.blob(f'MIDI/{firebase_file_name}')

    with open(local_file_path, 'rb') as local_file:
        blob.upload_from_file(local_file)

        if verbose:
            print(f"file {local_file_path} uploaded", file=sys.stderr)


if __name__ == "__main__":

    # test
    test_firebase_file_name = "diao_ye_zong.mid"

    # output file (path & name in Firebase Storage)
    test_blob = bucket.blob(f'MIDI/{test_firebase_file_name}')

    test_local_file_path = '../th07_05.mid'  # test

    with open(test_local_file_path, 'rb') as my_file:
        test_blob.upload_from_file(my_file)      # maybe add metadata ?
        print(f"file {test_local_file_path} uploaded")
