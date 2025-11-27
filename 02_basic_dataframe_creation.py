"""
FILE: 02_basic_dataframe_creation.py
PURPOSE: Learn how to create a DataFrame manually using dictionary data.
"""

import pandas as pd

# Creating a sample dataset using dictionary
data = {
    "Name": ['Ram', 'Raju', 'Rocky', 'John', 'Raki', 'Raju', 'Vicky', 'John'],
    "Age": [23, 54, 23, 43, 19, 34, 35, 64],
    "Salary": [20000, 30000, 43000, 42000, 29000, 54000, 35000, 46000],
    "Performance Score": [98, 34, 87, 67, 90, 97, 87, 89]
}

df = pd.DataFrame(data)

print("\n--- Manual DataFrame ---")
print(df)
