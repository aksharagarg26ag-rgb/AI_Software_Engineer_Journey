import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

df= pd.read_csv('ML/student_score.csv')
print(df)
X = df[["Hours"]]
Y = df["Score"]
print(X.shape)

X_train,X_test,Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=41)
model= LinearRegression()
model.fit(X_train, Y_train)

n= float(input("Enter hours: "))
prediction= model.predict([[n]])
print("Predicted Score:", prediction)

Y_pred= model.predict(X_test)

mae= mean_absolute_error(Y_test, Y_pred)
print("Mean Absolute Error:", mae)