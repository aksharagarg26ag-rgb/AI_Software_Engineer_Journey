from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("../student_score_linear.joblib")


class Hour(BaseModel):
    Hours: float


@app.post("/predict")
def predict(hours: Hour):

    features = [[hours.Hours]]

    prediction = model.predict(features)

    return {
        "predicted_score": float(prediction[0])
    }