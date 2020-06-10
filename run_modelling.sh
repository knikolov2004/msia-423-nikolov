winpty docker run -it --rm --mount type=bind,source="$(pwd)"/data,target=/data \
--mount type=bind,source="$(pwd)"/models/,target=/models/ \
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
spotify_classifier -W ignore modelling.py model