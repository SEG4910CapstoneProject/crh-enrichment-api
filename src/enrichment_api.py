from fastapi import FastAPI
from pydantic import BaseModel

from src.data_preprocessing import data_preprocessing

from pymongo import MongoClient
from src.config import *
import pickle
import base64

enrichment_api = FastAPI()

# Global variable to hold the ml model
ml_model = None

@enrichment_api.on_event("startup")
def load_model():
    global ml_model
    ml_model_name = "ML model"

    client = MongoClient("mongodb://{}:{}/".format(MONGO_HOST, MONGO_PORT), 
                                  username=MONGO_USERNAME, 
                                  password=MONGO_PASSWORD,
                                  uuidRepresentation='standard')
    collection = client[MONGO_DB_NAME][MONGO_ML_COLLECTION]
    data = collection.find_one({'name': ml_model_name})

    try:
        pickled_model = base64.b64decode(data['model'])
        ml_model = pickle.loads(pickled_model)
    except:
        raise Exception("Unable to load ML model from the database")

class articleData(BaseModel):
    title: str
    body: str


@enrichment_api.post("/models/v1/type")
def article_type(article: articleData):
    # Process the article content and title to get the ML model input 
    page_input = data_preprocessing(article.title, article.body)

    # Use the model to predict the model article type 
    global ml_model
    article_type = ml_model.predict([page_input])[0]

    # Prepare the response
    response = {
        "message": "Article processed successfully",
        "type": article_type
    }

    return response