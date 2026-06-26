import pandas as pd
import numpy as np

np.random.seed(42)

rows = []

for i in range(1000):

    income = np.random.randint(20000, 150000)
    age = np.random.randint(18, 60)
    credit_score = np.random.randint(300, 850)
    employment_years = np.random.randint(0, 20)

    if (
    income >= 40000
    and credit_score >= 600
    and employment_years >= 2
    ):
        approved = np.random.choice([1, 1, 1, 0])
    else:
        approved = np.random.choice([0, 0, 0, 1])

    rows.append([
        income,
        age,
        credit_score,
        employment_years,
        approved
    ])

df = pd.DataFrame(
    rows,
    columns=[
        "income",
        "age",
        "credit_score",
        "employment_years",
        "approved"
    ]
)

df.to_csv("loan_data.csv", index=False)

print(df.head())
print(df["approved"].value_counts())
print("Dataset Saved!")