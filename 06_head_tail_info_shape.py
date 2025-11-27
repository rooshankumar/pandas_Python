"""
FILE: 06_head_tail_info_shape.py
PURPOSE: Learn how to inspect DataFrame structure and basic metadata.
"""

import pandas as pd

df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

print("\n--- First 5 Rows (head) ---")
print(df.head())

print("\n--- Last 5 Rows (tail) ---")
print(df.tail())

print("\n--- DataFrame Info ---")
print(df.info())

print("\n--- Shape (rows, columns) ---")
print(df.shape)

print("\n--- Column Names ---")
print(df.columns)
