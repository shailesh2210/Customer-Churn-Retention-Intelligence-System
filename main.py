from src.logger.logger import logging
from src.components.data_ingestion import DataIngestion

# def main():
#     print("Hello from customer-churn-and-retention-intelligence-system!")

#     logging.info("Logging Begins")
    

if __name__ == "__main__":
    obj = DataIngestion()

    train_data , test_data = obj.initiate_data_ingestion()

    logging.info("Data Ingestion Completed")