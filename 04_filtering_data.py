"""
FILE: 04_filtering_data.py
PURPOSE: Learn how to filter rows using conditional logic in Pandas.
"""

import pandas as pd

# Sample dataset
data = {
    "Name": ['Ram', 'Raju', 'Rocky', 'John', 'Rani', 'Raju', 'Vicky', 'John'],
    "Age": [23, 54, 23, 43, 19, 34, 35, 64],
    "Salary": [20000, 30000, 43000, 42000, 29000, 54000, 35000, 46000],
    "Performance Score": [98, 34, 87, 67, 90, 97, 87, 89]
}

df = pd.DataFrame(data)

print("\n--- Dataset ---")
print(df)

# Filter: Salary > 50,000
print("\n--- Salary > 50K ---")
print(df[df["Salary"] > 50000])

# Filter: Salary > 50K AND Age > 40
print("\n--- Salary > 50K AND Age > 40 ---")
print(df[(df["Salary"] > 50000) & (df["Age"] > 40)])

# Filter: Salary > 50K OR Performance Score > 80
print("\n--- Salary > 50K OR Performance > 80 ---")
print(df[(df["Salary"] > 50000) | (df["Performance Score"] > 80)])
