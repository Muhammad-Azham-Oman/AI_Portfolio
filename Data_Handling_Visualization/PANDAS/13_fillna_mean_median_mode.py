import pandas as pd

df = pd.read_csv("wdata.csv")
mean = df["Calories"].mean()
a = df.fillna({"Calories" : mean})
print(a)


median = df["Calories"].median()
b = df.fillna({"Calories" : median})
print(b)


mode = df["Calories"].mode()[0]
c = df.fillna({"Calories" : median})
print(c)


# to chane the original data

df = pd.read_csv("wdata.csv")
mean = df["Calories"].mean()
d = df.fillna({"Calories" : mean},inplace=True)
print(d)