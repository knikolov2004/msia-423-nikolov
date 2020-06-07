import os
from os import path

"""
Every environment variable in this file is configured based on my choices - to run this file, you need to either
change the names of the environment variables on the machine this is being run on, or change the names in this file
"""

# Getting the parent directory of this file. That will function as the project home.
# PROJECT_HOME = path.dirname(path.dirname(path.abspath(__file__)))

# Logging
LOGGING_CONFIG = "config/logging.conf"

# SpotiPy variables
SP_USER = "1295675405"  # this is my public user id, not a key and needs to be passed as an argument to use my playlists
CID = os.environ.get("spotipy_cid")
SECRET = os.environ.get("spotipy_secret")

# Spotify variables
# these are all public, curated by me, and can be shared and used by whomever wishes to
WORKOUT_PL = "spotify:playlist:4C0Y70Mdqg6QuYhnlqNuZA"
DINNER_PL = "spotify:playlist:6aJRmDld7QjkjVF5zr8kTs"
SLEEP_PL = "spotify:playlist:7FKTT1OlLJe0GaQeG4WQW1"
PARTY_PL = "spotify:playlist:1rarcCQFwY40JpfpVBqjNh"
audio_feature_names = [
    'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
    'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'type',
    'id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature', 'playlist'
]

# Spotify raw features locations
WORKOUT_RAW_DATA = "workout_features.json"
DINNER_RAW_DATA = "dinner_features.json"
SLEEP_RAW_DATA = "sleep_features.json"
PARTY_RAW_DATA = "party_features.json"
WORKOUT_RAW_LOCATION = path.join('data/', WORKOUT_RAW_DATA)
DINNER_RAW_LOCATION = path.join('data/', DINNER_RAW_DATA)
SLEEP_RAW_LOCATION = path.join('data/', SLEEP_RAW_DATA)
PARTY_RAW_LOCATION = path.join('data/', PARTY_RAW_DATA)
FEATURES_RAW_LOCATION = "data/features.csv"

# RDS variables
user = os.environ.get("MYSQL_USER")
password = os.environ.get("MYSQL_PASSWORD")
host = os.environ.get("MYSQL_HOST")
port = os.environ.get("MYSQL_PORT")
database = os.getenv("DATABASE_NAME")
conn_type = "mysql+pymysql"
RDS_ENGINE_STRING = "{}://{}:{}@{}:{}/{}".format(conn_type, user, password, host, port, database)

# SQLITE env variables
LOCAL_DB = False # Change to True if you want it to write to local database instead of RDS
SQLITE_PATH = 'data/msia423_spotify_features.db'
SQLITE_ENGINE_STRING = "sqlite:////"+SQLITE_PATH

# S3 variables
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
S3_BUCKET = os.environ.get("S3_BUCKET")

# modelling parameters
training_features = [
    'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
    'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo'
]
target_feature = ['playlist']
test_size = 0.2
random_state = 1337
model_path = "models/lr.sav"
confusion_path = "models/confusion.csv"