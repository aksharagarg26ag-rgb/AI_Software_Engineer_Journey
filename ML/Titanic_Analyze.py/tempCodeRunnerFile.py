import pandas as pd
import joblib

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

df=pd.read_csv("titanic_dataset.csv")

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df.drop(columns=["Cabin"], inplace=True)
df["Sex"] = df["Sex"].map({ "male":0, "female":1})
df = pd.get_dummies(df,columns=["Embarked"],drop_first=True)

X = df.drop(columns=["PassengerId","Name","Ticket","Survived"])
y = df["Survived"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42)

logistic = LogisticRegression(max_iter=1000)

decision_tree = DecisionTreeClassifier(random_state=42)

random_forest = RandomForestClassifier(n_estimators=100,random_state=42)

logistic.fit(X_train, y_train)

decision_tree.fit(X_train, y_train)

random_forest.fit(X_train, y_train)

joblib.dump(
    logistic,
    "models/logistic.pkl"
)

joblib.dump(
    decision_tree,
    "models/decision_tree.pkl"
)

joblib.dump(
    random_forest,
    "models/random_forest.pkl"
)

print("All models saved successfully!")