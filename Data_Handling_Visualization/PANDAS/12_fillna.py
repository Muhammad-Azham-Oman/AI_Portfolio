import pandas as pd

# fill the null with the new value but d'nt change the orignal data
df = pd.read_csv("wdata.csv")
a = df.fillna(130)
print(a)

# fill the null with the new value but change the orignal data also
df = pd.read_csv("wdata.csv")
a = df.fillna(130,inplace=True)
print(a)


# fill the null with the new value in the specify column
df = pd.read_csv("wdata.csv")
a = df.fillna({"Calories":130})
print(a)


# fill the null with the new value in the specify column change the original data also
df = pd.read_csv("wdata.csv")
a = df.fillna({"Calories":130},inplace=True)
print(a)