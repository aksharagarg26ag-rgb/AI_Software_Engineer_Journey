
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

# Create:

# Bar chart of Top 10 Countries
# Bar chart of Top Ratings
import matplotlib.pyplot as plt

# Top 10 Countries
plt.subplot(1, 2, 1)
plt.bar(df["country"].value_counts().head(10).index, df["country"].value_counts().head(10).values)
plt.title("Top 10 Countries")
plt.xlabel("Country")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Top Ratings
plt.subplot(1, 2, 2)
plt.bar(df["rating"].value_counts().head(10).index, df["rating"].value_counts().head(10).values)
plt.title("Top 10 Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()