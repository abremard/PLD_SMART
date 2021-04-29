import firebase_admin
from firebase_admin import credentials, firestore
import string
from unidecode import unidecode

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
        genre: The string representing the track's genre
        artist: The track's artist
        file_ref: A string reference to the file in the Drive storage (format
                        to be defined)

    Returns: void

    """

    if file_ref is None:
        raise TypeError("Must provide a file_ref, provided None")

    # format inputs for database storage
    genre = "unknown" if genre is None else format_string(genre)
    artist = "unknown" if artist is None else format_string(artist)

    _add_genre_artist(genre, artist, file_ref)
    _add_artist(artist, file_ref)


def format_string(input_str: str):
    """
    Use this function to format an artist/a genre's string into the internal
    format used in the database

    Args:
        input_str: The string to format

    Returns: The formatted string

    """

    valid_chars = frozenset(f"-_ .!{string.ascii_letters}{string.digits}")
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
def _add_genre_artist(genre: str, artist: str, file_ref: str):
    genre_doc = db.collection(u"Tags").document(u"Genres")
    genre_doc.update({f"{genre}.{artist}": firestore.ArrayUnion([file_ref])})


def _add_artist(artist: str, file_ref: str):
    artist_doc = db.collection(u"Tags").document(u"Artists")
    artist_doc.update({artist: firestore.ArrayUnion([file_ref])})
