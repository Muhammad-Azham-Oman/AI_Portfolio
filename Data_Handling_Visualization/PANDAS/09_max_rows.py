import pandas as pd

df = pd.read_csv("data.csv")
print(pd.options.display.max_rows)



# to print the entire data

pd.options.display.max_rows = 99999
df = pd.read_csv("data.csv")
print(df)