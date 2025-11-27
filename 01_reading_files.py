"""
FILE: 01_reading_files.py
PURPOSE: Learn how to read different types of data files using Pandas.
"""

import pandas as pd

# -------------------------------
# 1. Reading a CSV File
# -------------------------------
print("\n--- Reading CSV File ---")
try:
    df_csv = pd.read_csv("sales_data_sample.csv", encoding="latin1")
    print(df_csv.head())
except FileNotFoundError:
    print("CSV file not found. Make sure 'sales_data_sample.csv' is in the same folder.")

# -------------------------------
# 2. Reading a JSON File
# -------------------------------
print("\n--- Reading JSON File ---")
try:
    df_json = pd.read_json("sample_Data.json", lines=True)
    print(df_json.head())
except FileNotFoundError:
    print("JSON file not found. Make sure 'sample_Data.json' is in the same folder.")

# -------------------------------
# 3. Reading an Excel File
# -------------------------------
print("\n--- Reading Excel File ---")
try:
    df_excel = pd.read_excel("sample.xlsx")
    print(df_excel.head())
except FileNotFoundError:
    print("Excel file not found. Place 'sample.xlsx' in the folder to test this.")
