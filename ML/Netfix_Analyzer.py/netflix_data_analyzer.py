import pandas as pd
df = pd.read_csv('ML/netflix.csv')
print("===== Netflix Analysis =====")
print("Total Movies: ", len(df[df["type"]== "Movie"]))
print("Total TV Shows: ", len(df[df["type"]== "TV Show"]))
print("Latest Release Year: ", df["release_year"].max())
print("Oldest Release Year: ", df["release_year"].min())
print("Top 10 Countries: ", df["country"].value_counts().head(10))
print("Top 10 Ratings: ", df["rating"].value_counts().head(10))
genres = df["listed_in"].str.split(", ")

all_genres = genres.explode()

print("Top Genre: ", all_genres.value_counts().head(1))

print("Groupby(): ", df.groupby("country").size())

print("Sorting: ", df.sort_values("release_year", ascending=False).head(5))