"""
FILE: 03_selecting_rows_columns.py
PURPOSE: Learn how to select rows and columns in a DataFrame.
"""

import pandas as pd

# Sample data
data = {
    "Name": ['Ram', 'Raju', 'Rocky', 'John'],
    "Age": [23, 54, 23, 43],
    "Salary": [20000, 30000, 43000, 42000]
}

df = pd.DataFrame(data)

print("\n--- Full DataFrame ---")
print(df)

# Selecting a single column (Series)
print("\n--- Selecting Single Column (Name) ---")
print(df["Name"])

# Selecting multiple columns
print("\n--- Selecting Multiple Columns (Name, Salary) ---")
print(df[["Name", "Salary"]])

# Selecting rows using iloc (index-based)
print("\n--- Selecting First Row (iloc) ---")
print(df.iloc[0])

# Selecting rows using loc (label-based)
print("\n--- Selecting Row with Index 2 (loc) ---")
print(df.loc[2])
