import numpy as np

number = np.arange(1,11)
fancy_indexing = number[2:8:2]
print(fancy_indexing)

where_number = np.where(number>5)
print(where_number)
print(number[where_number])

# Conditional array
''' understand it by if and else like the (number>5) is if condition and (number*4) is
when if is true and the (number) is in else.

Just like that:
if (number>5):
    print(number*4)
else:
    number'''

condition = np.where(number>5,number*4,number)
print(condition)