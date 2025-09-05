import pandas
a = [1,2,3]
d = a[0]
print(d)

b = pandas.Series(a)
c = pandas.Series(a,index=["x","y","z"])
print(b)
print(c["y"])

import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)
