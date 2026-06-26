import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

df = pd.read_csv("ML/titanic_dataset.csv", sep="\t")

print(df.head(5))
print(df.shape)
print(df.info())

print("Checking Null values: ")
print(df.isnull().sum())

print("Filling Null values... ")
df["Age"]= df["Age"].fillna(df["Age"].mean())
df["Embarked"]= df["Embarked"].fillna(df["Embarked"].mode()[0])

print("Dropping value... ")
df = df.drop(columns=["Cabin"])
    
print("After preprocessing:")
print(df.shape)
print(df.isnull().sum())

print("Encode Categorical Variables...")
df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)


X=df[["Pclass", "Age", "Fare", "Sex_male"]]
Y=df["Survived"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

scaler= StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test= scaler.transform(X_test)

model= LogisticRegression()
model.fit(X_train, Y_train)
 
Y_pred= model.predict(X_test)

accuracy= accuracy_score(Y_test, Y_pred)
print("Accuracy: ",accuracy*100,"%")


from sklearn.metrics import confusion_matrix
print(confusion_matrix(Y_test, Y_pred))

from sklearn.metrics import classification_report
print(classification_report(Y_test,Y_pred ))

#Feature Engineering: 
#FamilySize feature
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
survival_rate = df.groupby("FamilySize")["Survived"].mean()
print(survival_rate)

#Survival rate by Passenger Class
survival = df.groupby("Pclass")["Survived"].mean()
print(survival) 


#Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier

X = df[["Pclass","Age","Fare"]]
Y = df["Survived"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
rf= RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, Y_train)

predictions= rf.predict(X_test)
print(predictions)
Y_pred_rf= rf.predict(X_test)

accuracy_rf= accuracy_score(Y_test, Y_pred_rf)
print("Random Forest Accuracy: ", accuracy_rf*100, "%")


