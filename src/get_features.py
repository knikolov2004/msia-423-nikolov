import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import logging.config
from config.config import CID, SECRET, SP_USER, WORKOUT_PL, DINNER_PL, SLEEP_PL, PARTY_PL
from config.config import WORKOUT_RAW_LOCATION, DINNER_RAW_LOCATION, SLEEP_RAW_LOCATION, PARTY_RAW_LOCATION
import json

logger = logging.getLogger(__name__)
# Setting logger to debug for QA testing
logger.setLevel("DEBUG")

client_credentials_manager = SpotifyClientCredentials(client_id=CID, client_secret=SECRET)
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

    with open(file_location, "w+") as output_file:
        json.dump(records, output_file, indent=2)


if __name__ == "__main__":
    """
    The script fetches the target list of Spotify track URIs then iterates through the URIs to make a request for each
    URI to the Spotify features API. The resulting track features are persisted to a JSON file.
    """

    # Get track IDs for each playlist from Spotify API
    try:
        logger.debug("Fetching track ids")
        workout_tracks = get_track_ids(SP_USER, WORKOUT_PL)
        dinner_tracks = get_track_ids(SP_USER, DINNER_PL)
        sleep_tracks = get_track_ids(SP_USER, SLEEP_PL)
        party_tracks = get_track_ids(SP_USER, PARTY_PL)
    except Exception as e:
        logger.error("Error occurred while fetching track ids.", e)
        sys.exit(1)

    # Get Spotify features for each track
    workout_features = sp.audio_features(workout_tracks)
    dinner_features = sp.audio_features(dinner_tracks)
    sleep_features = sp.audio_features(sleep_tracks)
    party_features = sp.audio_features(party_tracks)

    # Persist raw features to file
    try:
        write_records(workout_features, WORKOUT_RAW_LOCATION)
        logger.info("%i workout_features written to %s", len(workout_features), WORKOUT_RAW_LOCATION)
    except FileNotFoundError:
        logger.error("Please provide a valid file location to persist data.")
        sys.exit(1)

    try:
        write_records(dinner_features, DINNER_RAW_LOCATION)
        logger.info("%i dinner_features written to %s", len(dinner_features), DINNER_RAW_LOCATION)
    except FileNotFoundError:
        logger.error("Please provide a valid file location to persist data.")
        sys.exit(1)

    try:
        write_records(sleep_features, SLEEP_RAW_LOCATION)
        logger.info("%i sleep_features written to %s", len(sleep_features), SLEEP_RAW_LOCATION)
    except FileNotFoundError:
        logger.error("Please provide a valid file location to persist data.")
        sys.exit(1)

    try:
        write_records(party_features, PARTY_RAW_LOCATION)
        logger.info("%i party_features written to %s", len(party_features), PARTY_RAW_LOCATION)
    except FileNotFoundError:
        logger.error("Please provide a valid file location to persist data.")
        sys.exit(1)
