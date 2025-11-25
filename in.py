import pandas as pd

df = pd.read_csv("sales_data_sample.csv", encoding="latin1")
print('Displaying the info of the Datasets')

print(df.info())