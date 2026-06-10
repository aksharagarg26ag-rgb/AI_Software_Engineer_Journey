import pandas as pd
df = pd.read_csv('Python/matplotlib_dataset.csv')
# print(df)

import matplotlib.pyplot as plt
# Line charts
plt.plot(df["Name"], df["Maths"])
plt.title("Maths Scores")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Bar charts
plt.bar(df["Name"], df["Maths"])
plt.title("Maths Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# histograms
plt.hist(df["Maths"])
plt.title("Maths Distribution")
plt.show()

# pie charts
total = df["Maths"] + df["Science"] + df["English"]

plt.pie(total, labels=df["Name"])

plt.title("Student Performance Share")

plt.show()


# scatter plots
plt.scatter(df["Maths"], df["Science"])

plt.xlabel("Maths")
plt.ylabel("Science")

plt.title("Maths vs Science")

plt.show()

# multiple graph subplots
plt.subplot(1,2,1)
plt.bar(df["Name"], df["Maths"])
plt.title("Maths")

plt.subplot(1,2,2)
plt.bar(df["Name"], df["Science"])
plt.title("Science")

plt.show()