import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import webbrowser

# Set up Spotify API credentials
client_id = "98cefb74f01e44ca9c80a8bf4eb7c0d2"
client_secret = "1579e41852b84a968c363cd08d103b81"

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))

def search_and_play(song_name):
    results = sp.search(q=song_name, limit=1, type='track')

    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        song_url = track['external_urls']['spotify']
        artist_name = track['artists'][0]['name']
        song_title = track['name']

        print(f"Found the song! Playing '{song_title}' by {artist_name}...")
        print(f"Spotify URL: {song_url}")
        webbrowser.open(song_url)
    else:
        print(f"Sorry, couldn't find the song '{song_name}'.")

# Get user input and search for the song
song_name = input("Enter the song name: ")
search_and_play(song_name)
