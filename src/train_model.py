import pandas as pd
import numpy as np
import json

import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn import model_selection
from sklearn import linear_model
from sklearn import metrics
import pickle
import logging
import config.config as c

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
logger = logging.getLogger(__file__)

def fit_scaler(dataframe):
    """
    Fit a standardizer on a dataframe to later be used on arrays
    Args:
        dataframe: dataframe which the scaler would calculate column means and variances on

    Returns: scaler object

    """
    scaler = StandardScaler()
    scaler.fit(dataframe)
    return scaler


def scale_data(dataframe, array):
    """
    Fits a scaler on a dataframe and applies it on an array of the same shape
    Args:
        dataframe: dataframe which the scaler would calculate column means and variances on
        array: array which will be standardized - needs to be same number of ordered vectors as the dataframe

    Returns: standardized array

    """
    scaler = fit_scaler(dataframe)
    return (array - scaler.mean_) / (scaler.var_ ** 0.5)


def train_model(model_dataframe):
    # standardizing the features we will be using for modelling
    features = scale_data(model_dataframe[c.training_features], model_dataframe[c.training_features])

    # creating train/test splits
    target = model_dataframe[c.target_feature]
    X_train, X_test, y_train, y_test = model_selection.train_test_split(
        features, target, test_size=c.test_size, random_state=c.random_state)

    # using logistic regression for this classification problem
    lr = linear_model.LogisticRegression(fit_intercept=False, penalty='l2')
    lr.fit(X_train, y_train)

    # saving the model to later use later on new data in the webapp
    logger.info("Saving model")
    try:
        pickle.dump(lr, open(c.model_path, 'wb'))
        logger.info("Model saved successfully")
    except:
        logger.error("Cannot save model - check if model exists and if path is correct")

    # fitting the model on test set
    # ypred_proba_test = lr.predict_proba(X_test)[:, 1]
    ypred_bin_test = lr.predict(X_test)

    # getting model results
    confusion = sklearn.metrics.confusion_matrix(y_test, ypred_bin_test)
    accuracy = sklearn.metrics.accuracy_score(y_test, ypred_bin_test)
    logger.info('Accuracy on test: %0.3f' % accuracy)
    index = []
    columns = []
    for i in model_dataframe.playlist.unique():
        actual = str('Actual ' + i)
        predicted = str('Predicted ' + i)
        index.append(actual)
        columns.append(predicted)
    pd.DataFrame(confusion,
                  index=index,
                  columns=columns)\
        .to_csv(c.confusion_path)

