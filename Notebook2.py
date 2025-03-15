#!/usr/bin/env python
# coding: utf-8

# In[1]:


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mlflow.sklearn
import pandas as pd

# Initialize FastAPI app
app = FastAPI(
    title="Banking ML Model API",
    description="API for predicting term deposit subscription using the best ML model from MLflow",
    version="1.0.0"
)

# Define the expected input schema using Pydantic
class InputData(BaseModel):
    age: int
    job: str
    marital: str
    education: str
    default: str
    balance: float
    housing: str
    loan: str
    contact: str
    day: int
    month: str
    duration: int
    campaign: int
    pdays: int
    previous: int
    poutcome: str

# Load the best model directly from MLflow artifact location
model_path = "C:/Users/user/MLOPS Project/mlruns/653138713369900692/06b5282264ed453f851a9ceda265ae95/artifacts/model"
try:
    model = mlflow.sklearn.load_model(model_path)
except Exception as e:
    raise RuntimeError(f"Failed to load the model: {e}")

@app.post("/predict", summary="Get Prediction", response_description="Prediction result")
def predict(input_data: InputData):
    """
    Accepts a JSON object containing input features,
    converts it to a DataFrame, and returns the model prediction.
    """
    try:
        # Convert input to DataFrame
        input_df = pd.DataFrame([input_data.dict()])
        
        # Make prediction
        prediction = model.predict(input_df)
        
        return {"prediction": prediction[0]}
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))



