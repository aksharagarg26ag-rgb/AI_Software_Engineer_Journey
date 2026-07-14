# # logistic regression:
# import pandas as pd
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score

# import joblib

# df = pd.read_csv("loan_data.csv")

# X= df[["Income","Age","CreditScore","EmploymentYears"]]
# Y=df["Approved"]

# X_train,X_test,Y_train,Y_test= train_test_split(X,Y, test_size=0.2, random_state=42)

# model = LogisticRegression(max_iter=1000)
# model.fit(X_train,Y_train)


# Y_pred= model.predict(X_test)
# accuracy= accuracy_score(Y_test,Y_pred)
# print("Accuracy : " ,accuracy * 100)

# Income= float(input("Enter income: "))
# Age= int(input("Enter age: "))
# CreditScore= int(input("Enter CreditScore: "))
# EmploymentYears = int(input("Enter EmploymentYears: "))
# new_data = pd.DataFrame({
#     "Income": [Income],
#     "Age": [Age],
#     "CreditScore": [CreditScore],
#     "EmploymentYears": [EmploymentYears]
# })

# prediction = model.predict(new_data)

# if prediction[0]==1:
#     print("Approved")

# else:
#     print("Not Approved")

# probability = model.predict_proba(new_data)
# print("Probability" ,probability)

# joblib.dump(model,"loan_data_model.joblib")
# print("Model Saved")


##RandomForestClassifier
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
from log.logger import logger
from sklearn.pipeline import Pipeline

#Load Dataset
df = pd.read_csv("data/loan_data.csv")
logger.info("Dataset loaded successfully!")

#Train Model
X= df[["income","age","credit_score","employment_years"]]
Y=df["approved"]

X_train,X_test,Y_train,Y_test= train_test_split(X,Y, test_size=0.2, random_state=42)

loan_pipeline = Pipeline([
    (
        "model",
        RandomForestClassifier(
            n_estimators=100,
            random_state=42
        )
    )
])
loan_pipeline.fit(X_train,Y_train)
logger.info("Model trained successfully!")

#Evaluate
Y_pred= loan_pipeline.predict(X_test)
accuracy= accuracy_score(Y_test,Y_pred)
logger.info(f"Model Accuracy : {accuracy * 100}%")

#Save Model
joblib.dump(loan_pipeline,"models/loan_pipeline.joblib")
logger.info("Model saved successfully!")

#to run this file open new terminal and run the command:  cd Projects/LoanApprovalSystem.py/backend and then python train_model.py