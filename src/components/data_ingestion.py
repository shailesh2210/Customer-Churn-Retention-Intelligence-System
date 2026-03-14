from src.logger.logger import logging
from pathlib import Path
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
import os

print("Hello World!")
logging.info("Logging has Started")

@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join("artifacts/", "train_data.csv")
    test_data_path = os.path.join("artifacts/", "test_data.csv")
    raw_data_path = os.path.join("artifacts/", "raw_data.csv")

class DataIngestion:

    def __init__(self):
        self.data_ingestion = DataIngestionConfig()

    def initiate_data_ingestion(self):

        logging.info("Enterned into the Data Ingestion")
        
        try:
            # path = Path("../data/raw_data.csv")
            data = pd.read_csv("data/raw_data.csv")

            os.makedirs(os.path.dirname(self.data_ingestion.raw_data_path), exist_ok = True)

            data.to_csv(self.data_ingestion.raw_data_path, index=False)

            logging.info("Raw Data Saved")

            train_data , test_data = train_test_split(data , test_size=0.2 , random_state=42)

            train_data.to_csv(self.data_ingestion.train_data_path, index = False)
            test_data.to_csv(self.data_ingestion.test_data_path, index = False)

            logging.info("Train Test Split Completed")

            return (
                self.data_ingestion.train_data_path,
                self.data_ingestion.test_data_path,
    
            )
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            raise