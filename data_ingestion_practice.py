import pandas as pd
import os
from sklearn.model_selection import train_test_split
import logging
import yaml

# ensure the "logs" directory exists, if not exist then make it using os.makedirs

log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)


# work with logging,   logging configuration

logger = logging.getLogger('data_ingestion')
logger.setLevel("DEBUG")

# consule handler
consule_handler= logging.StreamHandler()
consule_handler.setLevel('DEBUG')

# file handler
log_file_path = os.path.join(log_dir,'data_ingestion.log')
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel('DEBUG')

# formatter for both handlers
farmatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
consule_handler.setFormatter(farmatter)
file_handler.setFormatter(farmatter)

# add handlers to logger
logger.addHandler(consule_handler)
logger.addHandler(file_handler)

#define function for loading parameters
