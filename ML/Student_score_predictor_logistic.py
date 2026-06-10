import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df= pd.read_csv('ML/student_score_logisctic.csv')
X= df[["Hours"]]
Y=df["Pass"]

X_train,X_test,Y_train,Y_test= train_test_split(X,Y,test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, Y_train)

hours= float(input("Enter hours: "))
new_data = pd.DataFrame({"Hours": [hours]})
prediction= model.predict(new_data)
if prediction[0] == 1:
    print("Prediction: Pass")
else:
    print("Prediction: Fail")

probability = model.predict_proba(new_data)

print("\nProbability:")
print("Fail:", probability[0][0])
print("Pass:", probability[0][1])


Y_pred= model.predict(X_test)
accuracy = accuracy_score(Y_test, Y_pred)
print("Accuracy:", accuracy)