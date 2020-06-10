winpty docker run -it --rm --mount type=bind,source="$(pwd)"/data,target=/data \
--mount type=bind,source="$(pwd)"/models/,target=/models/ \
--env AWS_ACCESS_KEY_ID \
--env AWS_SECRET_ACCESS_KEY \
spotify_classifier -W ignore modelling.py model