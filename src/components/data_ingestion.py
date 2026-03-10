from src.logger.logger import logging
from pathlib import Path
import pandas as pd
from dataclasses import dataclass
import os

print("Hello World!")
logging.info("Logging has Started")

@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join("Artifacts", "train_data.csv")
    test_data_path = os.path.join("Artifacts", "test_data.csv")
    raw_data_path = os.path.join("Artifacts", "train_data.csv")

class DataIngestion:

    def __init__(self):
        self.data_ingestion = DataIngestionConfig

    def initiate_data_ingestion(self):
        
        try:
            data = pd.read_csv(os.path.join("data/", "raw_data.csv"))
            
        except:
            pass