import json
import re
import pandas as pd
import logging

import boto3
from botocore.exceptions import ClientError
import config.config as c

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
logger = logging.getLogger(__file__)


try:
    s3 = boto3.resource('s3', aws_access_key_id=c.AWS_ACCESS_KEY_ID, aws_secret_access_key=c.AWS_SECRET_ACCESS_KEY)
    logger.info("S3 Credentials Accepted.")
except ClientError as e:
    logging.error(e)


def read_json_s3(bucket, file):
    logger.info("Reading %s from %s", file, bucket)
    s3string = s3.Object(bucket, file).get()['Body'].read().decode('utf-8')
    s3json = json.loads(s3string)
    return s3json


def json_to_df(testjson, newcol):
    df = pd.DataFrame(testjson)
    df['playlist'] = newcol
    return df


def create_feature_df():
    logger.info("Creating database")
    # adding the 2 jsons to one dataframe with a new playlist column
    features = pd.DataFrame(columns=c.audio_feature_names)
    # raw_data = [c.DINNER_RAW_DATA, c.PARTY_RAW_DATA, c.SLEEP_RAW_DATA, c.WORKOUT_RAW_DATA]
    raw_data = [c.PARTY_RAW_DATA, c.CHILL_RAW_DATA]
    for file in raw_data:
        data = read_json_s3(c.S3_BUCKET, file)
        df = json_to_df(data, re.search("(.*)_", file).group(1).capitalize())
        features = features.append(df).reset_index().drop('index', axis=1)
    features.to_csv(c.FEATURES_RAW_LOCATION, index=False)
    return features

