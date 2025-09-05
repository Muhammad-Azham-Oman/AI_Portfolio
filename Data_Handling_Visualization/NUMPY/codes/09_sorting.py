import numpy as np

a = np.array([10,4,6,2,8,3,1,7,5,4,9,2,1])
print(np.sort(a))

# 2-D sorting

# row sorting
b = np.array([[3,2,6],[5,2,8]])
print(np.sort(b,axis=1))

# column sorting
b = np.array([[5,9,6],[3,2,8]])
print(np.sort(b,axis=0))