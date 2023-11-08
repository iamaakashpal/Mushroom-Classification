import logging
import os
from datetime import datetime

"""
Requirement for log
1. Log folder name
2. Log unique file name
3. Log file path
""" 

# Log folder name
LOG_FOLDER_NAME = 'logs'
os.makedirs(LOG_FOLDER_NAME,exist_ok=True)

# Unique Time
TIMESTAMP = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Log unique file name
LOG_FILE_NAME = f"logs_{TIMESTAMP}.log"

# Log file path
LOG_FILE_PATH = os.path.join(LOG_FOLDER_NAME,LOG_FILE_NAME)

# Basic config for logging
logging.basicConfig(
    filename = LOG_FILE_PATH,
    filemode = 'w',
    format = '[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO)

