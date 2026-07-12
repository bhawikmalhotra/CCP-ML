from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Create FastAPI app
app = FastAPI(title="Customer Churn Prediction API")

# Load trained pipeline
pipeline = joblib.load("models/churn_pipeline.joblib")


# Input Schema
class CustomerData(BaseModel):
    Partner: str
    Dependents: str
    Contract: str
    tenure: int
    MonthlyCharges: float
    OnlineSecurity: str
    TechSupport: str
    InternetService: str
    PaymentMethod: str


# Home Route
@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API is Running 🚀"
    }


# Prediction Route
@app.post("/predict")
def predict(data: CustomerData):

    # Convert input to DataFrame
    input_data = pd.DataFrame([data.model_dump()])

    # Prediction
    prediction = pipeline.predict(input_data)[0]

    # Probability
    probability = pipeline.predict_proba(input_data)[0][1]

    # Convert prediction to text
    result = "Customer Will Churn" if prediction == 1 else "Customer Will Stay"

    return {
        "prediction": result,
        "probability": round(float(probability), 2)
    }