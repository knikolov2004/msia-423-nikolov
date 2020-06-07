from src.clean_data import create_feature_df
from src.train_model import train_model

if __name__ == '__main__':
    features = create_feature_df()
    train_model(features)