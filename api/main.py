import pandas as pd
import pickle
from fastapi import FastAPI
from pydantic import BaseModel

with open('./models/best_optuna_model.pkl', 'rb') as f:
     model = pickle.load(f)

app = FastAPI(title='House Price Predictor')

class HouseFeatures(BaseModel):
    bedrooms: int
    bathrooms: float
    sqft_living: int
    sqft_lot: int
    floors: float
    condition: int
    sqft_basement: int
    pct_basement: float
    house_age: int
    renovation_age: int
    sqft_living15: int
    sqft_lot15: int
    city: str
    was_renovated: int

@app.post('/predict')
async def predict_price(features: HouseFeatures):
    # Convert input to DataFrame
    data = {
        'bedrooms': [features.bedrooms],
        'bathrooms': [features.bathrooms],
        'sqft_living': [features.sqft_living],
        'sqft_lot': [features.sqft_lot],
        'floors': [features.floors],
        'condition': [features.condition],
        'sqft_basement': [features.sqft_basement],
        'pct_basement': [features.pct_basement],
        'house_age': [features.house_age],
        'renovation_age': [features.renovation_age],
        'sqft_living15': [features.sqft_living15],
        'sqft_lot15': [features.sqft_lot15],
        'city': [features.city],
        'was_renovated': [features.was_renovated],
    }

    input_df = pd.DataFrame(data)

    # Predict
    prediction = model.predict(input_df)
    predicted_price = prediction.item()

    return predicted_price