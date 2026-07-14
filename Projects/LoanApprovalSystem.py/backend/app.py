import joblib
from fastapi import FastAPI
from pydantic import BaseModel
from logs.logger import logger


app= FastAPI()

loan_pipeline = joblib.load( "models/loan_pipeline.joblib")
logger.info("Model loaded!")

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

    
    prediction = loan_pipeline.predict(features)[0]
    logger.info(f"Prediction Result : {prediction}")
    
    probability = loan_pipeline.predict_proba(features)[0][1]
    return {
        "approved": bool(prediction),
        "probability": float(probability)
    }



# #
# import joblib
# from fastapi import FastAPI
# from pydantic import BaseModel
# import logging

# logging.basicConfig(
#     filename="logs/app.log",
#     level=logging.INFO,
#     format="%(asctime)s | %(levelname)s | %(message)s"
# )

# model = joblib.load("loan_data_rf.joblib")
# logging.info("Loan Approval Model Loaded Successfully")



# app= FastAPI()
# logging.info("Loan Approval API Started")

# class Loan(BaseModel):
#     income : float
#     age : int
#     credit_score : int
#     employment_years : float

# @app.post("/predict")
# def predict(loan: Loan):
#     try:
#         logging.info("Prediction Request Received")

#         logging.info(
#         f"Input -> Income:{loan.income}, "
#         f"Age:{loan.age}, "
#         f"Credit Score:{loan.credit_score}, "
#         f"Employment:{loan.employment_years}"
#         )

#         if loan.credit_score < 500:
#             logging.warning("Low Credit Score")
#         features= [[
#             loan.income,
#             loan.age,
#             loan.credit_score,
#             loan.employment_years
#         ]]
        
#         logging.info("Running ML Prediction")
#         prediction = model.predict(features)[0]
#         logging.info(f"Prediction Result : {prediction}")
        
#         return {
#             "approved": bool(prediction)
#         }

#     except Exception:

#         logging.exception("Prediction Failed")

#         return {
#             "error": "Internal Server Error"
#         }