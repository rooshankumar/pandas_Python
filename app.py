import pandas as pd

cf = pd.read_csv("sales_data_sample.csv", encoding="latin1")
print(cf)

jf = pd.read_json("sample_Data.json", lines=True)
print(jf)
