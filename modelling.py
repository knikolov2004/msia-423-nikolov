import argparse
from src.clean_data import create_feature_df
from src.train_model import train_model
import logging

logging.basicConfig(format='%(name)-12s %(levelname)-8s %(message)s', level=logging.INFO)
logger = logging.getLogger('modelling')

if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description="Transform Spotify raw data into a dataframe and classify to playlist")
    # parser.add_argument('step', help='Which step to run', choices=['transform', 'model', 'predict'])
    #
    features = create_feature_df()
    train_model(features)