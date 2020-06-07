import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import config.config as c
import json

import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
logger = logging.getLogger(__file__)

client_credentials_manager = SpotifyClientCredentials(client_id=c.CID, client_secret=c.SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = False


def get_track_ids(sp_user, playlist_uri):
    """Get individual URI's for each track in a Spotify playlist

    Args:
        sp_user (`str`): Spotify user URI
        playlist_uri (`str`): Spotify playlist URI

    Returns:
        id_list: comma separated list of track URI's
    """
    playlist = sp.user_playlist(sp_user, playlist_uri)
    tracks = playlist["tracks"]["items"]
    id_list = []
    for i in tracks:
        id_list.append(i["track"]["id"])
    return id_list


def write_records(records, file_location):
    """Persist API response set to file.

    Args:
        records (`:obj:`list` of :obj:`str`): The list of Spotify features.
        file_location (`str`): Location to write file to.

    Returns:
        None
    """

    if not file_location:
        raise FileNotFoundError

    num_records = len(records)
    logger.debug("Writing {} records to {}".format(num_records, file_location))
    try:
        with open(file_location, "w+") as output_file:
            json.dump(records, output_file, indent=2)
        logger.info("%i features written to %s", num_records, c.PARTY_RAW_LOCATION)
    except FileNotFoundError:
        logger.error("Please provide a valid file location to persist data.")
        sys.exit(1)


def get_features():
    """
    The script fetches the target list of Spotify track URIs then iterates through the URIs to make a request for each
    URI to the Spotify features API. The resulting track features are persisted to a JSON file.
    """
    logger.info("Getting tracks and features from Spotify API:")
    logger.debug(c.WORKOUT_RAW_LOCATION)
    # Get track IDs for each playlist from Spotify API
    try:
        logger.debug("Fetching track ids")
        workout_tracks = get_track_ids(c.SP_USER, c.WORKOUT_PL)
        dinner_tracks = get_track_ids(c.SP_USER, c.DINNER_PL)
        sleep_tracks = get_track_ids(c.SP_USER, c.SLEEP_PL)
        party_tracks = get_track_ids(c.SP_USER, c.PARTY_PL)
    except Exception as e:
        logger.error("Error occurred while fetching track ids.", e)
        sys.exit(1)

    # Get Spotify features for each track
    workout_features = sp.audio_features(workout_tracks)
    dinner_features = sp.audio_features(dinner_tracks)
    sleep_features = sp.audio_features(sleep_tracks)
    party_features = sp.audio_features(party_tracks)

    # Persist raw features to file
    write_records(workout_features, c.WORKOUT_RAW_LOCATION)
    write_records(dinner_features, c.DINNER_RAW_LOCATION)
    write_records(sleep_features, c.SLEEP_RAW_LOCATION)
    write_records(party_features, c.PARTY_RAW_LOCATION)
