import pandas as pd

df = pd.read_csv("wdata.csv")
print(df.duplicated())
print(df.drop_duplicates())


# With inplace = True
print(df.drop_duplicates())