import os 
from datetime import date

DATABASE_NAME = "VISA_"

COLLECTION_NAME = "visa_datasrt"

MONGODB_URL_KEY = "mongodb+srv://Abhi:Abhi1@cluste1.nwtqj7j.mongodb.net/?retryWrites=true&w=majority&appName=Cluste1"

PIPELINE_NAME: str = "us_visa"
ARTIFACT_DIR: str = "artifact"

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "visa_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2
