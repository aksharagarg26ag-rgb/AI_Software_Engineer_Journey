
import pandas as pd
df = pd.read_csv('ML/netflix.csv')
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
print(df["type"].value_counts())
print(df["release_year"].max())
print(df["release_year"].min())