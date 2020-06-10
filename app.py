import traceback
from flask import render_template, request, redirect, url_for
import logging.config
from flask import Flask
from src.create_db import Features
from flask_sqlalchemy import SQLAlchemy
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import pickle
import config.config as c
from src.train_model import scale_data
from flask_bootstrap import Bootstrap
import sklearn

# Initialize the Flask application
app = Flask(__name__, template_folder="app/templates")
Bootstrap(app)

# Configure flask app from flask_config.py
app.config.from_pyfile('config/flaskconfig.py')

# Define LOGGING_CONFIG in flask_config.py - path to config file for setting
# up the logger (e.g. config/logging/local.conf)
logging.config.fileConfig(app.config["LOGGING_CONFIG"])
logger = logging.getLogger(app.config["APP_NAME"])
logger.debug('Test log')

# Initialize the database
db = SQLAlchemy(app)


@app.route('/')
def index():
    """Main view that lists songs in the database.

    Create view into index page that uses data queried from Features database and
    inserts it into the app/templates/index.html template.

    Returns: rendered html template

    """

    try:
        features = db.session.query(Features).limit(app.config["MAX_ROWS_SHOW"]).all()
        logger.debug("Index page accessed")
        return render_template('index.html', features=features)
    except:
        traceback.print_exc()
        logger.warning("Not able to display tracks, error page returned")
        return render_template('error.html')


@app.route('/add', methods=['POST'])
def add_entry():
    """View that process a POST with new song input

    :return: redirect to index page
    """
    logger.info("Loading spotipy")
    client_credentials_manager = SpotifyClientCredentials(client_id=c.CID, client_secret=c.SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    sp.trace = False

    logger.info("Getting song details")
    song_details = sp.search(request.form['song_artist'])
    artist = song_details['tracks']['items'][0]['artists'][0]['name']
    track = song_details['tracks']['items'][0]['name']
    song_id = song_details['tracks']['items'][0]['id']

    logger.info("Classifying song")
    # import fitted model
    lr = pickle.load(open(c.model_path, 'rb'))
    song_features = sp.audio_features(song_id)
    df = pd.DataFrame(song_features)
    full_dataset = pd.read_csv(c.FEATURES_RAW_LOCATION)
    small_df = pd.DataFrame(scale_data(full_dataset[c.training_features], df[c.training_features]),
                            columns=c.training_features)
    ypred_bin_new = lr.predict(small_df)
    df['playlist'] = ypred_bin_new[0]
    df['artist'] = artist
    df['track'] = track
    logger.info("Song successfully classified")
    logger.info(df.dtypes)

    # try:
    song_rows = []
    for index, row in df.iterrows():
        song_row = Features(
            danceability=row.danceability,
            energy=row.energy,
            key=row.key,
            loudness=row.loudness,
            mode=row['mode'],
            speechiness=row.speechiness,
            acousticness=row.acousticness,
            instrumentalness=row.instrumentalness,
            liveness=row.liveness,
            valence=row.valence,
            tempo=row.tempo,
            type=row.type,
            id=row.id,
            uri=row.uri,
            track_href=row.track_href,
            analysis_url=row.analysis_url,
            duration_ms=row.duration_ms,
            time_signature=row.time_signature,
            playlist=row.playlist,
            artist=row.artist,
            track=row.track
        )
        song_rows.append(song_row)

    db.session.add_all(song_rows)
    db.session.commit()
    logger.info("New song added: %s by %s", track, artist)
    return redirect(url_for('index'))
    # except:
    #     logger.warning("Not able to display tracks, error page returned")
    #     return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=app.config["DEBUG"], port=app.config["PORT"], host=app.config["HOST"])
