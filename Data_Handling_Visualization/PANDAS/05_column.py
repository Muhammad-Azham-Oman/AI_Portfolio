import pandas as pd

df = pd.read_csv("data.csv")
df["salary"] = None
print(df)