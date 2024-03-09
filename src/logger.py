import sys
import os
import logging
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
Log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(Log_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(Log_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s -%(message)s",
    level=logging.INFO,
)


# if __name__ =="__main__":
#    logging.info("logging has started")