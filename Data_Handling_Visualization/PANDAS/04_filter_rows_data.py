import pandas as pd

df = pd.read_csv("data.csv")

junior_employees = df[df["Designation"]=="Junior"]
print(df.loc[17])
print(junior_employees)