import joblib
from fastapi import FastAPI
from pydantic import BaseModel


app= FastAPI()

model = joblib.load("loan_data_rf.joblib")
print("Model loaded!")

class Loan(BaseModel):
    income : float
    age : int
    credit_score : int
    employment_years : float

@app.post("/predict")
def predict(loan: Loan):
    features= [[
        loan.income,
        loan.age,
        loan.credit_score,
        loan.employment_years
    ]]

    
    prediction = model.predict(features)
    
    probability = model.predict_proba(features)
    return {
        "approved": bool(prediction[0]),
        "probability": float(probability[0][1])
    }