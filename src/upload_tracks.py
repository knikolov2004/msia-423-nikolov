import boto3
from botocore.exceptions import ClientError

import logging

logger = logging.getLogger(__name__)

import config.config as c

"""Creating s3 client for all functions in the file"""
try:
    s3 = boto3.client('s3', aws_access_key_id=c.AWS_ACCESS_KEY_ID, aws_secret_access_key=c.AWS_SECRET_ACCESS_KEY)
    logger.info("S3 Credentials Accepted.")
except ClientError as e:
    logging.error(e)


def upload_data_to_s3(bucket_name, local_file_path, s3_file_path):
    """ Upload data file to specified s3 bucket

    Args:
        bucket_name: :str: Name of s3 bucket

    Returns: Nothing
    """
    logger.info("Uploading %s to S3 %s bucket as %s:", local_file_path, bucket_name, s3_file_path)
    try:
        s3.upload_file(local_file_path, bucket_name, s3_file_path)
        logger.info("File successfully uploaded.")
    except:
        logger.debug(local_file_path)
        logger.error("Could not upload %s. Please check if the bucket name and local file path provided are valid",
                     s3_file_path)


def upload_all_tracks():
    """
    The script checks the config file for bucket name, local file paths and S3 file paths and uploads the local data
    to S3
    """
    logger.info("Starting to upload track features to S3:")
    upload_data_to_s3(c.S3_BUCKET, c.WORKOUT_RAW_LOCATION, c.WORKOUT_RAW_DATA)
    upload_data_to_s3(c.S3_BUCKET, c.SLEEP_RAW_LOCATION, c.SLEEP_RAW_DATA)
    upload_data_to_s3(c.S3_BUCKET, c.DINNER_RAW_LOCATION, c.DINNER_RAW_DATA)
    upload_data_to_s3(c.S3_BUCKET, c.PARTY_RAW_LOCATION, c.PARTY_RAW_DATA)
    upload_data_to_s3(c.S3_BUCKET, c.CHILL_RAW_LOCATION, c.CHILL_RAW_DATA)
