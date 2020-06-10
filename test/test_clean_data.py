from src.clean_data import json_to_df, create_feature_df
import config.config as c

import logging
logger = logging.getLogger(__name__)


def test_json_to_df_happy():
    testjson = {"test1": [2,3], "test2": [0,3]}
    try:
        json_to_df(testjson, "test3")
        logger.info("Test passed for json_to_df")
    except:
        logger.info("Test failed for json_to_df")


def test_json_to_df_unhappy():
    testjson = 'randomstring'
    try:
        json_to_df(testjson, "test3")
        logger.info("Test failed. This is not a json")
    except:
        logger.info("Test passed. This is not a json")


def test_create_feature_df_happy():
    try:
        create_feature_df()
        logger.info("Test passed, dataframe created.")
    except:
        logger.info("Test failed, erroneous input")