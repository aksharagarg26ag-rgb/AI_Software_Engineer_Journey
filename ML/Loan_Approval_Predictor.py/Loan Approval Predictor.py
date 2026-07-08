#Logistic Regression
import pandas as pd
from sklearn.model_selection import cross_val_score

from sklearn.linear_model import LogisticRegression

df= pd.read_csv('ML/Loan_Approval_Predictor.py/Loan Approval Predictor.csv')

X=df[["Income"]]
Y= df["Approved"]

model= LogisticRegression()

income=int(input("Enter your income: "))
new_data= pd.DataFrame({"Income": [income]})


scores = cross_val_score(
    model,
    X,
    Y,
    cv=5 
)

print("K-Fold Scores:", scores)
print("Average Accuracy:", scores.mean())






if prediction[0]==1:
    print("Approved!")
else:
    print("Not Approved.")

# probability = model.predict_proba(new_data)
# print("Approval Probability: ", probability[0][1]*100, "%")
# print("Not Approval Probability: ", probability[0][0]*100, "%")




#DecisionTree:
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import accuracy_score

# df= pd.read_csv('ML/Loan Approval Predictor.csv')

# X=df[["Income"]]
# Y= df["Approved"]

# X_train, X_test, Y_train, Y_test= train_test_split(X,Y, test_size=0.2, random_state=42)

# model= DecisionTreeClassifier(max_depth=3, random_state=42)
# model.fit(X_train, Y_train)

# income=int(input("Enter your income: "))
# new_data= pd.DataFrame({"Income": [income]})

# prediction= model.predict(new_data)

# if prediction[0]==1:
#     print("Approved!")
# else:
#     print("Not Approved.")


# Y_pred= model.predict(X_test)
# accuracy=accuracy_score(Y_test, Y_pred)
# print("Accuracy: ", accuracy)