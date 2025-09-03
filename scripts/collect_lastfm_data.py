import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()
LASTFM_API_KEY = os.getenv("LASTFM_API_KEY")

url = "http://ws.audioscrobbler.com/2.0/"
params = {
    "method": "geo.gettoptracks",
    "country": "United States",
    "limit": 50,
    "api_key": LASTFM_API_KEY,
    "format": "json"
}

response = requests.get(url, params=params)
data = response.json()

os.makedirs("data_raw/lastfm", exist_ok=True)
with open("data_raw/lastfm/US_top_tracks.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
