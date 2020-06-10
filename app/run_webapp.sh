winpty docker run -p 5000:5000 --name test \
--env SQLALCHEMY_DATABASE_URI \
--env spotipy_cid \
--env spotipy_secret \
--env AWS_ACCESS_KEY_ID \
--env AWS_SECRET_ACCESS_KEY \
spotify_playlist_app