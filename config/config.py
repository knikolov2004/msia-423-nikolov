import os
from os import path

# Getting the parent directory of this file. That will function as the project home.
PROJECT_HOME = path.dirname(path.dirname(path.abspath(__file__)))

# Spotipy variables
SP_USER = "1295675405" # this is my public user id, not a key and needs to be passed as an argument to use my playlists
CID = os.getenv("spotipy_cid")
SECRET = os.getenv("spotipy_secret")

# Spotify playlist URIs
# these are all public, curated by me, and can be shared and used by whomever wishes to
WORKOUT_PL = "spotify:playlist:4C0Y70Mdqg6QuYhnlqNuZA"
DINNER_PL = "spotify:playlist:6aJRmDld7QjkjVF5zr8kTs"
SLEEP_PL = "spotify:playlist:7FKTT1OlLJe0GaQeG4WQW1"
PARTY_PL = "spotify:playlist:1rarcCQFwY40JpfpVBqjNh"

# Spotify raw features locations
WORKOUT_RAW_LOCATION = path.join(PROJECT_HOME,'data/workout_features.json')
DINNER_RAW_LOCATION = path.join(PROJECT_HOME,'data/dinner_features.json')
SLEEP_RAW_LOCATION = path.join(PROJECT_HOME,'data/sleep_features.json')
PARTY_RAW_LOCATION = path.join(PROJECT_HOME,'data/party_features.json')