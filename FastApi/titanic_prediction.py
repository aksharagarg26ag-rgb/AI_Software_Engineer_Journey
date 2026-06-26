# from fastapi import FastAPI
# from pydantic import BaseModel
# app= FastAPI()
# class Passenger(BaseModel):
#     age: int
#     fare: float
# @app.post("/predict")
# def predict(passenger: Passenger):
#     if passenger.age < 18:
#         result = "child"

#     else:
#         result= "Adult"

#     return{
#         "prediction": result

#     }


## titanic_api
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("../titanic_rf.joblib")

class Passenger(BaseModel):
    Pclass: int
    Age: int
    Fare: float
    Sex: int

@app.post("/predict")
def predict(passenger: Passenger):

    features = [[
        passenger.Pclass,
        passenger.Age,
        passenger.Fare,
        passenger.Sex
    ]]

    prediction = model.predict(features)

    result = "Survived" if prediction[0] == 1 else "Did Not Survive"

    return {
        "prediction": result
    }