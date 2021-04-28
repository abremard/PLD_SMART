import firebase_admin
from firebase_admin import credentials, firestore

# ----------- Initialize Firebase connexion
# Use a service account
cred = credentials.Certificate("./cred.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


def add_entry(genre: str, artist: str, file_ref: str):
    """
    Use this function to add a new MIDI file's metadata (artist and genre) to
    the database.

    Args:
        genre: The music's genre in the following format: 'genre_name'
        artist: The track's artist in the following format: 'artist_name'
        file_ref: A string reference to the file in the Drive storage (format
                        to be defined)

    Returns: void

    TODO handle nulls and incorrect entries (reformat/replace)
    """
    _add_genre_artist(genre, artist, file_ref)
    _add_artist(artist, file_ref)


# --- internal functions - to be called together for db consistency and not by
#           the script's end user directly
def _add_genre_artist(genre: str, artist: str, file_ref: str):
    genre_doc = db.collection(u"Tags").document(u"Genres")
    genre_doc.update({f"{genre}.{artist}": firestore.ArrayUnion([file_ref])})


def _add_artist(artist: str, file_ref: str):
    artist_doc = db.collection(u"Tags").document(u"Artists")
    artist_doc.update({artist: firestore.ArrayUnion([file_ref])})
