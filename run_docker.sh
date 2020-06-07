# shell file to streamline system env collection
docker run -it --rm --mount type=bind,source="$(pwd)"/data,target=/data \
--env MYSQL_HOST \
--env MYSQL_PORT \
--env MYSQL_USER \
--env MYSQL_PASSWORD \
--env DATABASE_NAME \
--env spotipy_cid \
--env spotipy_secret \
--env aws_access_key_id \
--env aws_secret_access_key \
spotify_classifier ingestion.py