import pandas as pd

df = pd.read_csv("sales_data_sample.csv",encoding="latin1")
#HIS Method
# print(df.head())
# print(df.info())
# print(df.shape)

data = {
    "Name" : ['Roshan', 'Komal', 'Raju'],
    "Age" : [21, 24, 34]
}

sf = pd.DataFrame(data)
             
# print(sf)

row = sf["Name"]
# print(row)

row2 = sf[['Name','Age']]
# print(row2)

# print(sf.loc[1])
filter = sf[sf['Age'] > 30]
print(filter)

filter2 = sf[(sf['Name'] == 'Komal') & (sf['Age'] > 20)]
print(filter2)

print(sf.describe())
print(df.describe())
print(df.tail())
print(df.head())
print(df.mode())