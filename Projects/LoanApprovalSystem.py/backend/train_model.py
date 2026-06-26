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


df = pd.read_csv("loan_data.csv")
print(df.shape)

print(df["approved"].value_counts())
X= df[["income","age","credit_score","employment_years"]]
Y=df["approved"]

X_train,X_test,Y_train,Y_test= train_test_split(X,Y, test_size=0.2, random_state=42)

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train,Y_train)


Y_pred= rf.predict(X_test)
accuracy= accuracy_score(Y_test,Y_pred)
print("Accuracy : " ,accuracy * 100, "%")

income= float(input("Enter income: "))
age= int(input("Enter age: "))
credit_score= int(input("Enter CreditScore: "))
employment_years = int(input("Enter EmploymentYears: "))
new_data = pd.DataFrame({
    "income": [income],
    "age": [age],
    "credit_score": [credit_score],
    "employment_years": [employment_years]
})


prediction = rf.predict(new_data)
if prediction[0]==1:
    print("Approved")

else:
    print("Not Approved")

probability = rf.predict_proba(new_data)
print("Probability" ,probability)


joblib.dump(rf,"loan_data_rf.joblib")
print("Model Saved")