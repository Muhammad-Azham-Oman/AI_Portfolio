import pandas as pd

df = pd.read_csv("data.csv")
a = df["Salary"].mean()
print(a)

b = df["Salary"].mode()
print(b)

c = df["Salary"].median()
print(c)

c = df["Salary"].median()
print(c)