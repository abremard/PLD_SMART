from database.metadata_processing.spotify_api import *
from database.metadata_processing.sort_functions import *


def main():

    # --- spotify test
    print(get_artist_genre("the hu"))

    # --- chanian's test
    # sort_midi_files("midi_directory")


if __name__ == '__main__':
    main()
