import pandas as pd

df = pd.read_csv("data.csv")
print(df)


# to view the entire dataframe:

df = pd.read_csv("data.csv")
print(df.to_string())