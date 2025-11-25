import pandas as pd

data = {
    "Name" : [ 'Ram', 'Shyam', 'Rocky'],
    "Age" : [10,20,30],
    "City" : [ 'Nagpur', 'Delhi', 'Agra']
}

df = pd.DataFrame(data)
print(df)

# df.to_csv("output.csv", index=False)

# df.to_excel("output2.xlsx", index=False)

df.to_json("output.json", index=False)
