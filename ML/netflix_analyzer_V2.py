import pandas as pd
df = pd.read_csv('ML/netflix.csv')
print("===== Netflix Analysis =====")
print("Menu: ")
print("1. Top Countries ")
print("2. Top Directors")
print("3. Content by Year")
print("4. Content by Rating")
print("5. Exit")

while True:
    choice= int(input("Enter your choice: "))
    
    if(choice==1):
        top_country = int(input("Enter number of required top countries: "))
        print("Top Countires : ", df["country"].value_counts().head(top_country))

    elif(choice==2):
        top_directors = int(input("Enter number of required top directors: "))
        print("Top Directors : ", df["director"].value_counts().head(top_directors))

    elif(choice==3):
        print(" Content by Year" , df.groupby(["release_year"]).size().sort_values(ascending=False))

    elif(choice==4):
        top_ratings = int(input("Enter number of required top ratings: "))
        print("Top Ratings : ", df["rating"].value_counts().head(top_ratings))

    elif(choice==5):
        print("Exiting...")
        break
