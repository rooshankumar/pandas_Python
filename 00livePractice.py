import pandas as pd

df = pd.read_csv("messy_restaurant_data.csv")
# print(df)
# print(df.head())
# print(df.info())
# print(df.shape)
# print(df.isnull())
# print(df.fillna("Unknown"))

# print(df.isnull().sum())
# print(df.dropna())
# print(df.dropna(axis=1))
# print(df.isnull().sum())
# df = df.fillna("OKAY")
# print(df)
# print(df.duplicated())
# print(df.duplicated().sum())
# df = df.drop_duplicates()
# print(df)
# df = df.drop_duplicates(subset=["Restaurant_Name"])
# print(df)
# df.columns = df.columns.str.replace(" ", "_")
# print(df.columns)

# df["Rating"] = (
#     df["Rating"]
#     .astype(str)
#     .str.lower()
#     .str.strip()
#     .str.extract(r'(\d+\.?\d*)')
# )
# df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")
# print(df["Rating"])


# df["Restaurant_Name"] =(
#     df["Restaurant_Name"]
#     .str.lower()
#     .str.replace(r"\s+", " ", regex=True)
#     .str.strip()
#     .str.title()

# )
# print(df["Restaurant_Name"])


# df["City"] = (
#     df["City"]
#     .astype(str)
#     .str.lower()
#     .str.strip()
#     .str.replace(r"\s+", " ",regex=True)
#     .replace({
#         "banglore" : "bangalore",
#         "hyderbad" : "hyderabad"
#     })
#     .str.title()

# )

# print(df["City"])

# df["Cuisine"] = (
#     df["Cuisine"]
#     .astype(str)
#     .str.lower()
#     .str.strip()
#     .str.replace(r"\s+", " ", regex=True)
#     .str.replace("-", " ")
#     .replace({
#         "chineese" : "chinese",
#         "nan" : pd.NA
#     })
#     .str.title()

# )
# print(df["Cuisine"])

df["Price"] = (
    df["Price"] 
    .astype(str)
    .str.lower()
    .str.replace(r"[₹$]","", regex=True)
    .str.replace(r"rs|inr", "", regex=True)
    .str.replace(r'\s+', " ", regex=True)
    .str.strip()
    .replace({
        "one hundred" : 100,
        "two hundred" : 200,
        "three hundred" : 300
    })
    .str.extract(r"(\d+\.?\d*)")

)
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
print(df["Price"])