import firebase_admin
from firebase_admin import credentials, firestore
import string
from unidecode import unidecode
import os
import sys


"""
TODO add genre in artists document
"""

db = None


def init_firebase_connexion(verbose=True):
    if verbose:
        print("Initializing Firebase connexion...", file=sys.stderr)
    # ----------- Initialize Firebase connexion
    dirname = os.path.dirname(__file__)
    credentials_file = os.path.join(dirname, './cred.json')

    cred = credentials.Certificate(credentials_file)
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'ilolio.appspot.com'       # default bucket, maybe change for a custom bucket later
    })
    global db
    db = firestore.client()
    if verbose:
        print("Firebase connexion successfully initiated.", file=sys.stderr)


def add_entry(file_ref: str, genre: str, artist: str, *instruments: str):
    """
    Use this function to add a new MIDI file's metadata (artist and genre) to
    the database.

    Args:
        file_ref: A string reference to the file in the Firestore storage
        genre: The string representing the track's genre
        artist: The track's artist
        *instruments: Strings corresponding to instrument(s) present in the
                        track
                        
    Raises TypeError if the file provided is None

    Returns: void

    """

    if db is None:
        raise Exception("Firebase connexion not initialized. Please use init_firebase_connexion before caling this function.")

    if file_ref is None:
        raise TypeError("Must provide a file_ref, provided None")

    # format inputs for database storage
    formatted_genre = "unknown" if genre is None else format_string(genre)
    formatted_artist = "unknown" if artist is None else format_string(artist)
    formatted_instruments = []
    for i, instrument in enumerate(instruments):
        # todo maybe remove formatting if already done before this step
        formatted_instruments.append("unknown" if instrument is None else format_string(instrument))

    # print(f"formatted values: {formatted_artist}, {formatted_genre}, {formatted_instruments}")

    _add_genre_artist(formatted_genre, formatted_artist, artist, file_ref)
    _add_artist(formatted_artist, artist, file_ref)

    for instrument in formatted_instruments:
        _add_instrument(instrument, file_ref)

    _add_track(file_ref, formatted_genre, formatted_artist, artist, *formatted_instruments)


def reset_database(confirm=True):

    if db is None:
        raise Exception("Firebase connexion not initialized. Please use init_firebase_connexion before caling this function.")

    if confirm:
        user_confirm = input("WARNING: Reset database content? (Y/N): ")
        if user_confirm not in ('y', 'Y'):
            print("Cancelled database reset.")
            return

    print("Resetting database...")
    # reset documents
    db.collection('Tags').document('Artists').set({})
    db.collection('Tags').document('Genres').set({})
    db.collection('Tags').document('Instruments').set({})
    db.collection('Tags').document('Tracks').set({})


def format_string(input_str: str):
    """
    Use this function to format an artist/a genre's string into the internal
    format used in the database

    Args:
        input_str: The string to format

    Returns: The formatted string

    """

    valid_chars = frozenset(f"-_ {string.ascii_letters}{string.digits}")
    # replace accents
    res = unidecode(input_str)
    # keep only valid characters
    res = ''.join(c for c in res if c in valid_chars)
    # lowercase only
    res = res.lower()
    # and replace spaces with _
    res = res.replace(" ", "_")
    return res


# --- internal functions - to be called together for db consistency and not by
#           the script's end user directly
def _add_genre_artist(genre: str, formatted_artist: str, artist_name:str, file_ref: str):
    genre_doc = db.collection(u"Tags").document(u"Genres")
    genre_doc.update({f"{genre}.{formatted_artist}.tracks": firestore.ArrayUnion([file_ref]),
                      f"{genre}.{formatted_artist}.name": artist_name})


def _add_artist(formatted_artist: str, artist_name: str, file_ref: str):
    artist_doc = db.collection(u"Tags").document(u"Artists")
    artist_doc.update({f"{formatted_artist}.tracks": firestore.ArrayUnion([file_ref]), f"{formatted_artist}.name": artist_name})


def _add_instrument(instrument: str, file_ref: str):
    instruments_doc = db.collection(u"Tags").document(u"Instruments")
    instruments_doc.update({instrument: firestore.ArrayUnion([file_ref])})


def _add_track(file_ref: str, genre: str, artist: str, artist_name: str, *instruments: str):
    file_ref = file_ref.split('.')[0].split('/')[-1]
    # print(f"file ref: {file_ref}")
    tracks_doc = db.collection(u"Tags").document(u"Tracks")
    tracks_doc.update({f"{file_ref}.artist": artist, f"{file_ref}.genre": genre, f"{file_ref}.artist_name": artist_name,
                       f"{file_ref}.instruments": firestore.ArrayUnion([ins for ins in instruments])})
