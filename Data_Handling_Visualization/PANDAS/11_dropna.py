import pandas as pd

# remove the empty rows and d'nt change the original data
df = pd.read_csv("wdata.csv")
b = df.dropna()
print(b)



# remove the empty rows and change the original data also
df = pd.read_csv("wdata.csv")
b = df.dropna(inplace=True)
print(b)


# to remove the null from specific column
df = pd.read_csv("wdata.csv")
a = df.dropna(subset=["Date"])
print(a)