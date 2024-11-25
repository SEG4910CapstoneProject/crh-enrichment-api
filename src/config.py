import os

#API Variables
ENRICHMENT_HOST = os.getenv("ENRICHMENT_HOST", "0.0.0.0")
ENRICHMENT_PORT = os.getenv("ENRICHMENT_PORT", 8000)

# Db Variables
MONGO_PORT = os.getenv('MONGO_PORT', "27017")
MONGO_HOST = os.getenv('MONGO_HOST', "localhost")
MONGO_USERNAME = os.getenv('MONGO_USERNAME')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')
MONGO_DB_NAME = os.getenv('MONGO_DB_NAME')
MONGO_ML_COLLECTION = os.getenv('MONGO_ML_COLLECTION', "ml_model")