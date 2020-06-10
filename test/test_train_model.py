from src.train_model import fit_scaler, scale_data
import pandas as pd
import numpy as np

import logging
logger = logging.getLogger(__name__)

def test_fit_scaler_happy():
    df = pd.DataFrame({"col1":[1,2,3], "col2":[3,6,9]})
    try:
        fit_scaler(df)
        logger.info("Test passed, scaler fit")
    except:
        logger.info("Test failed, input is not a dataframe")

def test_fit_scaler_unhappy():
    df = "randomstring"
    try:
        fit_scaler(df)
        logger.info("Test failed, string cannot be fit")
    except:
        logger.info("Test passed, input is not a dataframe")

def test_scale_data_happy():
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": [3, 6, 9]})
    array = np.array([[1,1], [2,2]])
    try:
        scale_data(df, array)
        logger.info("Test passed, array scaled")
    except:
        logger.info("Test failed, array couldn't be scaled")

def test_scale_data_unhappy():
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": [3, 6, 9]})
    array = np.array([[1,1,1],[2,2,2]])
    try:
        scale_data(df, array)
        logger.info("Test failed, cannot scale array of different dimensions")
    except:
        logger.info("Test passed, cannot scale array of different dimensions")