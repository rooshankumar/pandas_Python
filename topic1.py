
'''
1. how big is your Dataset?
2. what are the names of the columns?
 
shape and columns
'''
import pandas as pd

data = {
    "Name" : ['Ram', 'Raju', 'Rocky', 'John', 'Raki', 'Raju', 'Vicky', 'John'],
    "Age" : [23,54,23,43,19,34,35,64],
    "Salary" : [20000, 30000, 43000, 42000, 29000, 54000, 35000, 46000],
    "Performance Score" : [ 98,34,87,67,90,97,87,89]
}

df = pd.DataFrame(data)
print("Data Frame Manual")
print(df)

print("Another Space")

print(f'Space :{df.shape}')
print(f'Column :{df.columns}')