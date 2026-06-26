import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df= pd.read_csv("ML/Sttudent_Score.py/student_score.csv", )

X = df[["Hours"]]
Y = df["Score"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model= LinearRegression()
model.fit(X_train, Y_train)

##
joblib.dump(model,"student_score_linear.joblib")
print("Model Saved")

model = joblib.load("student_score_linear.joblib")

print(type(model))