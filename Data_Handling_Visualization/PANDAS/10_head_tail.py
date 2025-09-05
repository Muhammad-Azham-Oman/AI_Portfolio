import pandas as pd

df = pd.read_csv("data.csv")
print(df.head())
print(df.tail())

print(df.head(10))
print(df.tail(10))