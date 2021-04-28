import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

with open("./spotify_credentials.txt", 'r') as credentials_file:
    # parse credentials from the credentials file
    client_id = credentials_file.readline().strip()
    client_secret = credentials_file.readline().strip()

    # authenticate on Spotify
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    print("Connected", file=sys.stderr)


def get_artist_genre(input_artist: str) -> str:

    """
    TODO replace _ with spaces ?
    Args:
        input_artist: Name of the artist (format TBD)

    Returns: The artist's first genre as a string

    """

    results = sp.search(q='artist:' + input_artist, type='artist')
    artists = results['artists']['items']

    if len(artists) > 0:
        with open("./output_spotipy.json", 'w') as out_file:
            out_file.write(json.dumps(artists, indent=4))
            out_file.close()

        # artist = artists[0]
        # print(artist['name'], artist['images'][0]['url'])
        # print(artist)

        names = []
        for artist in artists:
            names.append(artist['name'])

        best_index = _best_match_index(input_artist, names)
        print(f"best match (out of {len(artists)} match(es)): {artists[best_index]['name']}", file=sys.stderr)
        genres = artists[best_index]['genres']
        if len(genres) > 0:
            return genres[0]        # arbitrary choice

    # if there was an error somewhere
    return "unknown"


def _best_match_index(reference: str, matches) -> int:
    min_dist = 100000
    best_index = -1

    for i, match in enumerate(matches):
        dist = len(match) - len(reference)    # TODO use Levenshtein distance here
        if dist < min_dist:
            best_index = i
            min_dist = dist

    return best_index
