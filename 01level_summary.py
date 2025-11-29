import pandas as pd

# ---------------------------------------
# 1) Reading Files
# ---------------------------------------

# Read a CSV file (common in real datasets)
df_csv = pd.read_csv("sales_data_sample.csv", encoding="latin1")

# Read a JSON file (line-delimited JSON)
df_json = pd.read_json("sample_Data.json", lines=True)


# ---------------------------------------
# 2) Creating a Basic DataFrame Manually
# ---------------------------------------

data = {
    "Name": ['Ram', 'Raju', 'Rocky', 'John', 'Rani'],
    "Age":  [23, 54, 23, 43, 19],
    "Salary": [20000, 30000, 43000, 42000, 29000],
}

df = pd.DataFrame(data)


# ---------------------------------------
# 3) Selecting Columns & Rows
# ---------------------------------------

# Select a single column (returns a Series)
names = df["Name"]

# Select multiple columns (returns a DataFrame)
name_salary = df[["Name", "Salary"]]

# Filter rows based on a condition
high_salary = df[df["Salary"] > 40000]

# Multiple conditions (AND)
high_salary_age = df[(df["Salary"] > 40000) & (df["Age"] > 30)]

# OR condition
salary_or_performance = df[(df["Salary"] > 30000) | (df["Age"] < 25)]


# ---------------------------------------
# 4) Basic Statistics
# ---------------------------------------

# Quick descriptive statistics for numbers
stats = df.describe()

# ---------------------------------------
# 5) Head, Tail, Info, Shape
# ---------------------------------------

top_rows = df.head()        # first 5 rows
bottom_rows = df.tail()     # last 5 rows
info = df.info()            # column types, non-null info
shape = df.shape            # (rows, columns)

# ---------------------------------------
# Final Print (optional)
# ---------------------------------------
print(df)
print(names)
print(name_salary)
print(high_salary)
