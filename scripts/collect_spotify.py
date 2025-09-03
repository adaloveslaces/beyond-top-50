import requests
import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

CLIENT_ID = client_id
CLIENT_SECRET = client_secret

url = "https://accounts.spotify.com/api/token"
data = {
    "grant_type": "client_credentials",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET
}

response = requests.post(url, data=data)
token = response.json()["access_token"]

SPOTIFY_TOKEN = token
OUTPUT_DIR = 'data_raw/spotify_top_songs'
os.makedirs(OUTPUT_DIR, exist_ok=True)

PLAYLISTS = {
    'Pop': '0zRBnQGhf1IqokuhnISG97',  
    'Hip-Hop': '6uzQMUvSWUuchYAgfz9O3K', 
    'Rock': '61jNo7WKLOIQkahju8i0hw',
    'Country' : '4Jb4PDWREzNnbZcOHPcZPy',
    'Jazz': '5rdgRwdMskt1IJKjNf0VWQ'
}

def get_headers():
    return {"Authorization": f"Bearer {SPOTIFY_TOKEN}"}

def get_playlist_tracks(playlist_id):
    tracks = []
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?limit=100"
    while url:
        response = requests.get(url, headers=get_headers())
        response.raise_for_status()
        data = response.json()
        tracks.extend(data['items'])
        url = data['next']
    return tracks

def save_tracks_to_file(genre, tracks):
    filename = os.path.join(OUTPUT_DIR, f"{genre}_top_songs.json")
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(tracks, f, ensure_ascii=False, indent=2)

def main():
    for genre, playlist_id in PLAYLISTS.items():
        tracks = get_playlist_tracks(playlist_id)
        save_tracks_to_file(genre, tracks)

if __name__ == "__main__":
    main()
