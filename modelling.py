import argparse
import pandas as pd
import logging

from src.clean_data import create_feature_df
from src.train_model import train_model


logging.basicConfig(format='%(name)-12s %(levelname)-8s %(message)s', level=logging.INFO)
logger = logging.getLogger('modelling')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Transform Spotify raw data into a dataframe and classify to playlist")
    parser.add_argument('step', help='Which step to run', choices=['transform', 'model', 'predict'])
    parser.add_argument('--input', '-i', default=None, help='Path to input data')
    parser.add_argument('--output', '-o', default=None, help='Path to save output CSV (optional, default = None)')
    args = parser.parse_args()

    if args.step == 'transform':
        features = create_feature_df()
    if args.step == 'model':
        if args.output is not None:
            if args.input is not None:
            #having both input and output
                try:
                    features = pd.read_csv(args.input)
                    logger.info('Input data loaded from %s', args.input)
                except:
                    logger.error("Wrong file path!")
                train_model(features, output=args.output)
            #having output but no input
            else:
                features = create_feature_df()
                train_model(features, output=args.output)
        else:
            #having no output no input
            if args.input is None:
                features = create_feature_df()
                train_model(features)


