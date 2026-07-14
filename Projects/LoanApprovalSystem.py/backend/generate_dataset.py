import pandas as pd
import numpy as np
from logs.logger import logger

np.random.seed(42) #every time when run the code, it will generate the same random numbers.

rows = []
logger.info("Generating dataset...")

for i in range(1000):

    income = np.random.randint(20000, 150000)
    age = np.random.randint(18, 60)
    credit_score = np.random.randint(300, 850)
    employment_years = np.random.randint(0, 20)

    MIN_INCOME = 40000
    MIN_CREDIT_SCORE = 600
    MIN_EMPLOYMENT_YEARS = 2

    if (
    income >= MIN_INCOME
    and credit_score >= MIN_CREDIT_SCORE
    and employment_years >= MIN_EMPLOYMENT_YEARS
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

logger.info("Dataset generated and saved!")

print(df.head())
print(df["approved"].value_counts())
