"""
TODO:
    - add a Songs collection to access metadata for a given file
"""
from database.firestore.utils_firestore import *
from database.firestore.upload_midi import *
from database.firestore.db_postprocessing import *


def main():
    init_firebase_connexion()

    # ----- tests
    # reset_database()
    # add_entry("Highway_to_Hell.mid", "Rock", "AC/DC", "Guitar")
    # add_entry("Megalovania.mid", "Game music", "Toby Fox", "Piano")
    # add_entry("Dance_of_Eternity.mid", "Progressive Metal", "Dream Theater", "Drums", "Guitar")

    # res = format_string("Làé'ifj")
    # print(res)
    pass


if __name__ == '__main__':
    main()
