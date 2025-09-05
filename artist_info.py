import os
import sys
import spotipy

from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials

"""
Get Information about Artist (Spotipy Example Code)
"""
def get_artist_info(sp, name):
    artist_info = sp.search(q='artist:' + name, type='artist')
    items = artist_info['artists']['items']
    return items[0] if items else None

"""
Get 5 Most Recent Albums by Artist
"""
def get_recent_albums(sp, artist):
    albums = []
    results = sp.artist_albums(artist['id'], album_type='album', limit=5)
    albums.extend(results['items'])

    # Skip Duplicate Items
    unique = set()
    for album in albums:
        name = album['name']
        if name not in unique:
            unique.add(name)
            
    return unique

"""
Get Artist's Top Tracks (10 by Default)
"""
def get_top_tracks(sp, artist):
    results = sp.artist_top_tracks(artist['id'])
    return results['tracks']

def print_artist_data(sp, artist, albums, tracks):
    # Print Artist Info
    print(f"Artist: {artist['name']}")
    print(f"Genre: {artist['genres']}")
    print(f"Followers: {artist['followers']['total']}")
    print(f"Popularity (1-100): {artist['popularity']}")
    
    # Print Recent Albums
    print("\nAlbums:")
    for idx, album in enumerate(albums):
        print(f"{idx+1}: {album}")
    
    # Print Top Songs
    print("\nTop Tracks:")
    for idx, track in enumerate(tracks):
        print(f"{idx+1}: {track['name']}")

def main():
    if (len(sys.argv) > 1):
        # Load .env values
        load_dotenv()
        id = os.getenv('CLIENT_ID')
        secret = os.getenv('CLIENT_SECRET')

        # Initialize Spotify API 
        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(id, secret))
        name = ""
        
        if (len(sys.argv) > 2):
            for i in range(1, len(sys.argv)):
                name += (sys.argv[i] + " ")
        else:
            name = sys.argv[1]

        artist = get_artist_info(sp=sp, name=name)

        # Get albums, top tracks, then output
        if artist:
            albums = get_recent_albums(sp=sp, artist=artist)
            tracks = get_top_tracks(sp=sp, artist=artist)
            print_artist_data(sp=sp, artist=artist, albums=albums, tracks=tracks)
        else:
            print(f"Couldn't find artist {name}")
    else:
        print("No Artist Selected")

if __name__ == "__main__":
    main()
