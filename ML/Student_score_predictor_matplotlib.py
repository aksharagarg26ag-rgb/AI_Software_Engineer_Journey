import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df= pd.read_csv("ML/student_score.csv")

#scatter plot
plt.scatter(df["Hours"], df["Score"])
plt.title("Hours vs Score")
plt.xlabel("Hours")
plt.ylabel("Score")
plt.show()

#regression line
plt.scatter(df["Hours"], df["Score"])
m, b = np.polyfit(df["Hours"], df["Score"], 1) 
plt.plot(df["Hours"], m*df["Hours"] + b, color='red')
plt.title("Hours vs Score with Regression Line")
plt.xlabel("Hours")
plt.ylabel("Score")
plt.show()
