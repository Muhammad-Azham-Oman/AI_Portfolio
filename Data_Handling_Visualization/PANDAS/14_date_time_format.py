import pandas as pd

df = pd.read_csv("wdata.csv")
df["Date"] = pd.to_datetime(df['Date'],format='mixed')
print(df)