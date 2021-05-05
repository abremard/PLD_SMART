"""
Functions used to post-process the database
"""

import sys
from src.database.firestore import *
from firebase_admin import *
import firebase_admin
import json
from typing import Dict


# def rename_tracks():
#     db = firestore.client()
#     tracks_ref = db.collection('Tags').document('Tracks')
#     tracks: Dict = tracks_ref.get().to_dict()
#
#     for key, value in tracks.items():
#         print(f"{key}: {value}")


def fuse_genres(*genres: str, new_name: str):
    """
    Renames all provided genres to new_name in the database.
    Use this if you are not happy with genres provided by Spotify's API after
    uploading MIDI files without specifying a genre.

    Args:
        *genres: The exact names of the genres to rename as they appear in Firebase
        new_name: The exact name that the provided genres should be renamed to in Firebase

    Returns: void

    """

    print(f"Fusing genres {genres} to {new_name}")

    for genre in genres:
        rename_genre(genre, new_name)
    pass


def rename_genre(old_name: str, new_name: str):
    """
    Renames the genre old_name to new_name in the database.
    Use this if you are not happy with the genre provided by Spotify's API after
    uploading MIDI files without specifying a genre.

    Args:
        old_name: The exact name of the genre to rename as it appears in Firebase
        new_name: The exact name that the provided genre should be renamed to in Firebase

    Returns: void

    """

    print(f"Renaming genre {old_name} to {new_name}")

    db = firestore.client()
    genres_ref = db.collection('Tags').document('Genres')
    artists_ref = db.collection('Tags').document('Artists')
    tracks_ref = db.collection('Tags').document('Tracks')
    genres = genres_ref.get()

    if genres.exists:

        doc_dict = genres.to_dict()
        genre_content = doc_dict[old_name]

        # backup file, delete later
        with open("./backup_file.json", 'a+') as backup_file:
            backup_file.write(json.dumps(genre_content, indent=4))

        # dictionary for bulk update in Tracks document
        bulk_update_tracks = {}

        if genre_content is not None:  # genre found, everything ok

            # print(f"Genre content: {genre_content}")

            for artist in genre_content.keys():
                # add artist data to new genre
                print(f"updating {new_name}.{artist}")
                genres_ref.update({f"{new_name}.{artist}": genre_content[artist]})

                # rename genre in artist doc (actually does not exist yet)
                # artists_ref.update({f"{artist}.genre": new_name})     # todo add genre field in other artist items?

                for track in genre_content[artist]['tracks']:
                    bulk_update_tracks[f"{track.split('/')[-1].split('.')[0]}.genre"] = new_name

            # print(f"Bulk updating tracks document with dictionary: {bulk_update_tracks}")
            print(f"Bulk updating tracks document...")
            tracks_ref.update(bulk_update_tracks)

            # delete old field
            print("Deleting old field")
            genres_ref.update({old_name: firestore.DELETE_FIELD})  # todo uncomment this

        else:  # genre not found
            raise Exception(f"Error: Genre {old_name} does not exist.")

    else:  # should not happen
        raise Exception("Error: collection Genres does not exist.")


# def move_artist_to_new_genre(todo):
#     # todo
#     pass


if __name__ == '__main__':

    init_firebase_connexion()

    if len(sys.argv) == 3:
        rename_genre(sys.argv[1], sys.argv[2])
    elif len(sys.argv) > 3:
        fuse_genres(*sys.argv[1:-1], new_name=sys.argv[-1])
    else:
        raise Exception("Error: Please provide at least one name of genre to rename and the new genre name")

    # rename_tracks()
