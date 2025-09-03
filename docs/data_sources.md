# Data Sources & Collection Methods

## Spotify Web API
- Endpoint: https://accounts.spotify.com/api/token
- Query: Tracks by playlist
- Authentication: OAuth 2.0 Client Credentials flow (using client ID and secret)
- Rate limits: ~20 requests per second
- Raw data saved: `data_raw/spotify_top_songs`
- Collection script: `scripts/collect_spotify.py`

## Last.fm API
- Endpoint: http://ws.audioscrobbler.com/2.0/
- Method: geo.gettopartists (top artists in US)
- Parameters: country name, limit of artists returned
- Authentication: API key via query string
- Rate limits: Polite 1-second delay between calls added
- Raw data saved: `data_raw/lastfm`
- Collection script: `scripts/collect_lastfm_data.py`


