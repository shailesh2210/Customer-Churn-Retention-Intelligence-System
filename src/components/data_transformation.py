import pandas as pd
from src.logger.logger import logging
from sklearn.preprocessing import LabelEncoder
import os


class DataTransformationConfig:

    preprocessor_file_obj_path = os.path.join("artifacts/" , "preprocessor.pkl")


class DataTransfomer:

    def __init__(self):
        self.data_transfomation_config = DataTransformationConfig()

    def data_transformation(Self):

        try:
            
            logging.info("Data Transformation Started!!")


        except Exception as e:
            pass