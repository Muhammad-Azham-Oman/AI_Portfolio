import pandas as pd

df = pd.read_csv("data.csv")

a = df[df["Salary"]] = df["Salary"].max()
print(a)

b = df[df["Salary"]] = df["Salary"].min()
print(b)