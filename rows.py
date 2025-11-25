#head() #tail()
#head(n) #tail()

import pandas as pd

df = pd.read_csv("sales_data_sample.csv", encoding="latin1")
print('Display 10 rows of first')
print(df.head())

print('Display 10 tails of last')
print(df.tail())
