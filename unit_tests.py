import logging

from test.test_clean_data import test_json_to_df_happy, test_json_to_df_unhappy, test_create_feature_df_happy
from test.test_train_model import test_fit_scaler_happy, test_fit_scaler_unhappy, test_scale_data_happy, test_scale_data_unhappy

logging.basicConfig(format='%(name)-12s %(levelname)-8s %(message)s', level=logging.INFO)
logger = logging.getLogger('ingestion')

if __name__ == '__main__':
    test_json_to_df_happy()
    test_json_to_df_unhappy()
    test_create_feature_df_happy()
    test_fit_scaler_happy()
    test_fit_scaler_unhappy()
    test_scale_data_happy()
    test_scale_data_unhappy()