winpty docker run -p 5000:5000 --name test \
--env MYSQL_HOST \
--env MYSQL_PORT \
--env MYSQL_USER \
--env MYSQL_PASSWORD \
--env DATABASE_NAME \
--env spotipy_cid \
--env spotipy_secret \
--env AWS_ACCESS_KEY_ID \
--env AWS_SECRET_ACCESS_KEY \
--env S3_BUCKET \
spotify_playlist_app