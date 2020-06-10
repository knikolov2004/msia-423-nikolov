import json
import re
import pandas as pd
import logging

import boto3
from botocore.exceptions import ClientError
import config.config as c

logger = logging.getLogger(__name__)


try:
    s3 = boto3.resource('s3', aws_access_key_id=c.AWS_ACCESS_KEY_ID, aws_secret_access_key=c.AWS_SECRET_ACCESS_KEY)
    logger.info("S3 Credentials Accepted.")
except ClientError as e:
    logging.error(e)


def read_json_s3(bucket, file):
    """
    Collects data from s3 bucket and returns loaded json file
    Args:
        bucket: S3 bucket name
        file: file path in s3 bucket

    Returns: loaded json file

    """
    logger.info("Reading %s from %s", file, bucket)
    s3string = s3.Object(bucket, file).get()['Body'].read().decode('utf-8')
    s3json = json.loads(s3string)
    return s3json


def json_to_df(testjson, newcol):
    """Reads json file and returns dataframe with columns based on keys. Creates new "playlist" column based on input"""
    try:
        df = pd.DataFrame(testjson)
    except:
        logger.error("The file is not a json/cannot be read as a dataframe!")
    df['playlist'] = newcol
    return df


def create_feature_df():
    """
    Merges all loaded jsons into 1 dataframe with playlist column
    Returns: merged dataframe

    """
    logger.info("Creating dataframe")
    # adding the 2 jsons to one dataframe with a new playlist column
    features = pd.DataFrame(columns=c.audio_feature_names)
    raw_data = [c.PARTY_RAW_DATA, c.CHILL_RAW_DATA]
    for file in raw_data:
        data = read_json_s3(c.S3_BUCKET, file)
        df = json_to_df(data, re.search("(.*)_", file).group(1).capitalize())
        features = features.append(df).reset_index().drop('index', axis=1)
    features.to_csv(c.FEATURES_RAW_LOCATION, index=False)
    return features

