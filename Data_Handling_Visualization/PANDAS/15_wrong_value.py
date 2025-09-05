import pandas as pd

df = pd.read_csv("wdata.csv")
df.loc[7,"Duration"] = 45

# or set the data for wrong format

for i in df.index:
    if df.loc[i,"Duration"]>120:
        df.loc[i,"Duration"]=120

# to delete the row for wrong format
for i in df.index:
    if df.loc[i,"Duration"]>120:
        df.drop(i,inplace=True)

# or filter the data
df = df[df["Duration"]<=120]

print(df)