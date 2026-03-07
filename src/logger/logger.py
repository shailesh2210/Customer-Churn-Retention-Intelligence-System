import os
import logging
from datetime import datetime

log_file = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

log_path = os.path.join(os.getcwd(), "Logs" , log_file)
os.makedirs(log_path , exist_ok=True)

Log_file_path = os.path.join(log_path , log_file)

logging.basicConfig(
    filename=Log_file_path,
    format= f"[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)