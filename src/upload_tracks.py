import boto3
import logging.config

logger = logging.getLogger(__name__)
# raw data names
from config.config import WORKOUT_RAW_DATA, SLEEP_RAW_DATA, DINNER_RAW_DATA, PARTY_RAW_DATA
# raw data local paths
from config.config import WORKOUT_RAW_LOCATION, SLEEP_RAW_LOCATION, DINNER_RAW_LOCATION, PARTY_RAW_LOCATION
# s3 bucket name
from config.config import S3_BUCKET


def upload_data_to_s3(bucket_name, local_file_path, s3_file_path):
    """ Upload data file to specified s3 bucket

    Args:
        bucket_name: :str: Name of s3 bucket

    Returns: Nothing
    """
    logger.info("Uploading %s to S3 %s bucket as %s:", local_file_path, bucket_name, s3_file_path)
    s3 = boto3.resource("s3")
    bucket = s3.Bucket(bucket_name)
    try:
        bucket.upload_file(local_file_path, s3_file_path)
        logger.info("File successfully uploaded.")
    except:
        logger.error("Could not upload file. Please check if the bucket name and local file path provided are valid.")


if __name__ == "__main__":
    """
    The script checks the config file for bucket name, local file paths and S3 file paths and uploads the local data 
    to S3
    """
    upload_data_to_s3(S3_BUCKET, WORKOUT_RAW_LOCATION, WORKOUT_RAW_DATA)
    upload_data_to_s3(S3_BUCKET, SLEEP_RAW_LOCATION, SLEEP_RAW_DATA)
    upload_data_to_s3(S3_BUCKET, DINNER_RAW_LOCATION, DINNER_RAW_DATA)
    upload_data_to_s3(S3_BUCKET, PARTY_RAW_LOCATION, DINNER_RAW_DATA)
