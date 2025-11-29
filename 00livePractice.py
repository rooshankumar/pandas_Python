import pandas as pd

df = pd.read_csv("students_performance_level3.csv")
# print(df.head())
# print(df.info())
# print(df.shape)
print(df["full_name"])
print(df[["full_name"]])
print(type(df["full_name"]))
print(type(df[["full_name"]]))
