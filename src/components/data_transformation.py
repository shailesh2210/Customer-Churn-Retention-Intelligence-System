import pandas as pd
from src.logger.logger import logging
from sklearn.preprocessing import LabelEncoder
from src.utils import save_obj
import os


class DataTransformationConfig:

    preprocessor_file_obj_path = os.path.join("artifacts/" , "preprocessor.pkl")


class DataTransfomer:

    def __init__(self):
        self.data_transfomation_config = DataTransformationConfig()

    def data_transformation(Self, df):

        try:
            
            logging.info("Data Transformation Started!!")


            df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")


        except Exception as e:
            pass