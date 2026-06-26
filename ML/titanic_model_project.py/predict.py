import joblib
model = joblib.load("titanic_rf.joblib")

# Sample passenger

passenger = [[
    1,      # Pclass
    25,     # Age
    100,     # Fare
    1       # Female
]]

prediction = model.predict(passenger)

if prediction[0] == 1:
    print("Passenger Survived")
else:
    print("Passenger Did Not Survive")
