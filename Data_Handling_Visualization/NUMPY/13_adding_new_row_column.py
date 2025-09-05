import numpy as np

a = np.array([[1,2,3],[4,5,6]])

# row addition

new_row = np.array([7,8,9])
with_new_row = np.vstack((a,new_row))
print("Without new row", a)
print("With_new_row", with_new_row)

# column addition

new_column = np.array([[7],[8]])
with_new_column = np.hstack((a,new_column))
print("Without new column", a)
print("With_new_column", with_new_column)