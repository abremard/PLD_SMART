import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import os

global sp
sp = None


def init_spotify_connexion(verbose=True):
    """
    Call this function once before calling functions that use Spotify's API

    Args:
        verbose: Set to True for mor prints

    Returns: void

    """

    dirname = os.path.dirname(__file__)
    spotify_credentials_path = os.path.join(dirname, './spotify_credentials.txt')

    with open(spotify_credentials_path, 'r') as credentials_file:
        # parse credentials from the credentials file
        client_id = credentials_file.readline().strip()
        client_secret = credentials_file.readline().strip()

        # authenticate on Spotify
        auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        global sp
        sp = spotipy.Spotify(auth_manager=auth_manager)
        if verbose:
            print("Connected to Spotify API endpoint", file=sys.stderr)


def get_artist_genre(input_artist: str, verbose=False) -> str:
    global sp
    """
    TODO replace _ with spaces ?
    Args:
        input_artist: Name of the artist (format TBD)
        verbose: set to True to run prints (False by default)

    Returns: The artist's first genre as a string

    """

    if sp is None:
        raise Exception(
            "Spotify connexion not initialized. Please use init_spotify_connexion before caling this function.")

    results = sp.search(q='artist:' + input_artist, type='artist')
    artists = results['artists']['items']

    if len(artists) > 0:
        cur_dir = os.path.dirname(__file__)
        output_path = os.path.join(cur_dir, "./output_spotipy.json")
        with open(output_path, 'w') as out_file:
            out_file.write(json.dumps(artists, indent=4))
            out_file.close()

        names = []
        for artist in artists:
            names.append(artist['name'])

        best_index = _best_match_index(input_artist, names)
        if verbose:
            print(f"best match (out of {len(artists)} match(es)): {artists[best_index]['name']}", file=sys.stderr)

        genres = artists[best_index]['genres']
        if len(genres) > 0:
            return genres[0]  # arbitrary choice

    # if there was an error somewhere
    return "unknown"


def _best_match_index(reference: str, matches) -> int:
    min_dist = 100000
    best_index = -1

    for i, match in enumerate(matches):
        dist = len(match) - len(reference)  # TODO use Levenshtein distance here
        if dist < min_dist:
            best_index = i
            min_dist = dist

    return best_index
