import pandas as pd

# Load original messy CSV
df = pd.read_csv("messy_restaurant_data.csv")

# ------------------------------
# 1) Missing Values
# ------------------------------

# Quick check of how many missing values each column has
print(df.isnull().sum())

# Example: fill missing city values with a placeholder
df["City"] = df["City"].fillna("Unknown")


# ------------------------------
# 2) Duplicate Rows
# ------------------------------

# Count duplicate rows
print(df.duplicated().sum())

# Remove exact duplicate entries
df = df.drop_duplicates()


# ------------------------------
# 3) Clean Column Names
# ------------------------------

# Make column names consistent: lowercase + underscores
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)


# ------------------------------
# 4) Clean Restaurant Name
# ------------------------------

df["restaurant_name"] = (
    df["restaurant_name"]
    .astype(str)
    .str.lower()                    # standardize case
    .str.replace(r"\s+", " ", regex=True)  # collapse multiple spaces
    .str.strip()                    # remove spaces at start/end
    .str.title()                    # make readable
)


# ------------------------------
# 5) Clean City Column
# ------------------------------

df["city"] = (
    df["city"]
    .astype(str)
    .str.lower()
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)
    # fix known spelling mistakes manually
    .replace({
        "banglore": "bangalore",
        "hyderbad": "hyderabad"
    })
    .str.title()
)


# ------------------------------
# 6) Clean Cuisine Column
# ------------------------------

df["cuisine"] = (
    df["cuisine"]
    .astype(str)
    .str.lower()
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)
    .str.replace("-", " ")              # unify hyphens and spaces
    .replace({
        "chineese": "chinese",          # correct bad spelling
        "nan": pd.NA                    # convert 'nan' string → actual NaN
    })
    .str.title()
)


# ------------------------------
# 7) Clean Price Column
# ------------------------------

df["price"] = (
    df["price"]
    .astype(str)
    .str.lower()
    .str.strip()
    # remove currency symbols
    .str.replace(r"[₹$]", "", regex=True)
    # remove currency words
    .str.replace(r"rs|inr", "", regex=True)
    # clean spacing
    .str.replace(r"\s+", " ", regex=True)
    # convert some number words to digits before extraction
    .replace({
        "one hundred": "100",
        "two hundred": "200",
        "three hundred": "300"
    })
    # pull out the numeric part (e.g., 250.00, 4.5, 300)
    .str.extract(r"(\d+\.?\d*)")
)

# Convert final cleaned price into numeric dtype
df["price"] = pd.to_numeric(df["price"], errors="coerce")


# ------------------------------
# Final Output
# ------------------------------
print(df)
