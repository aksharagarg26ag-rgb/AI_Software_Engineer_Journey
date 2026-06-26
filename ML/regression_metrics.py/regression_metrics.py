import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import( mean_absolute_error, mean_squared_error)

df= pd.read_csv("ML/regression_metrics_dataset.csv")

X=df[["YearsExperience"]]
Y=df["Salary"]

X_train,X_test, Y_train, Y_test= train_test_split(X,Y, test_size=0.2, random_state=42)

model= LinearRegression()
model.fit(X_train, Y_train)

y_pred = model.predict(X_test)

mae= mean_absolute_error(Y_test, y_pred)
mse= mean_squared_error(Y_test, y_pred)
rmse = np.sqrt(mse)

print("MAE :", mae)
print("MSE :", mse)
print("RMSE:", rmse)