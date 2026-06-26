import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


df= pd.read_csv("ML/titanic_dataset.csv", sep="\t")

X= df[["Pclass", "Age", "Fare", "Sex"]]
Y= df["Survived"]

X["Age"]=X["Age"].fillna(X["Age"].mean())
X["Sex"]=X["Sex"].map({ "male": 0, "female":1})

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

rf= RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, Y_train)

##\
joblib.dump(rf,"titanic_rf.joblib")
print("Model Saved")