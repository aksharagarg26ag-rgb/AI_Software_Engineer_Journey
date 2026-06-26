import pandas as pd
df = pd.read_csv('ML/netflix.csv')

print("Missing Values")
print(df.isnull())
print(df.isnull().sum())

print("Filling missing value of director")
df["director"]= df["director"].fillna("Unknown")
print(df["director"].isnull().sum())

print("droping missing values")
print(df.dropna())

print("Duplicate rows")
print(df.duplicated())
print(df.duplicated().sum())
print(df.drop_duplicates())

print(df.shape)