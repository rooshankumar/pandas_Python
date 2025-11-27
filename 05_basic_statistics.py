"""
FILE: 05_basic_statistics.py
PURPOSE: Learn how to generate descriptive statistics using Pandas.
"""

import pandas as pd

data = {
    "Name": ['Ram', 'Raju', 'Rocky', 'John', 'Rani', 'Raju', 'Vicky', 'John'],
    "Age": [23, 54, 23, 43, 19, 34, 35, 64],
    "Salary": [20000, 30000, 43000, 42000, 29000, 54000, 35000, 46000],
    "Performance Score": [98, 34, 87, 67, 90, 97, 87, 89]
}

df = pd.DataFrame(data)

print("\n--- Full DataFrame ---")
print(df)

print("\n--- Descriptive Statistics (Numerical Columns) ---")
print(df.describe())

print("\n--- Mean Salary ---")
print(df["Salary"].mean())

print("\n--- Median Age ---")
print(df["Age"].median())

print("\n--- Mode of Name Column ---")
print(df["Name"].mode())
