import boto3
from botocore.exceptions import ClientError

import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
logger = logging.getLogger(__file__)

# raw data names
from config.config import WORKOUT_RAW_DATA, SLEEP_RAW_DATA, DINNER_RAW_DATA, PARTY_RAW_DATA
# raw data local paths
from config.config import WORKOUT_RAW_LOCATION, SLEEP_RAW_LOCATION, DINNER_RAW_LOCATION, PARTY_RAW_LOCATION
# s3 variables
from config.config import S3_BUCKET, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

try:
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
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
    upload_data_to_s3(S3_BUCKET, WORKOUT_RAW_LOCATION, WORKOUT_RAW_DATA)
    upload_data_to_s3(S3_BUCKET, SLEEP_RAW_LOCATION, SLEEP_RAW_DATA)
    upload_data_to_s3(S3_BUCKET, DINNER_RAW_LOCATION, DINNER_RAW_DATA)
    upload_data_to_s3(S3_BUCKET, PARTY_RAW_LOCATION, PARTY_RAW_DATA)
