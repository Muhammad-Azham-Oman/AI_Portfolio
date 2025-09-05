import pandas as pd

df = pd.read_csv("data.csv")
a = df.info()
print(a)

b = df.describe(include='all')
print(b)

c = df.head()
print(c)

d = df.head()
print(d)