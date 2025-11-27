import pandas as pd

data = {
    "Name" : ['Ram', 'Raju', 'Rocky', 'John', 'Rani', 'Raju', 'Vicky', 'John'],
    "Age" : [23,54,43,43,19,34,35,64],
    "Salary" : [20000, 30000, 93000, 42000, 29000, 54000, 35000, 46000],
    "Performance Score" : [ 98,44,87,67,90,97,87,89]
}

df = pd.DataFrame(data)
# print("Data Frame Manual")
# print(df)

high_Salary = df[df['Salary'] > 50000]
print("Employees with salary more than 50K")
print(high_Salary)

high_Salary2 = df[(df['Salary'] > 50000) & (df['Age'] > 40)]
print("Employees with salary more than 50K and age more than 40")
print(high_Salary2)

performace = df[(df['Salary'] > 50000) | (df['Performance Score'] > 40)]
print("Employees with salary more than 50K OR performance more than 40")
print(performace)