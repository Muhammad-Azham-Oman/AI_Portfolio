import numpy as np

# For 1-D array

a = np.arange(1,11)

print("Index slicing: ", a[3])
print("Negative index slicing: ", a[-3])
print("Basic slicing: ", a[2:8])
print("Step slicing: ", a[2:8:2])
print("Negative slicing: ", a[-5:-2])

# For 2-D array

arr = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

print("Spcific element: ", arr[1,2])
print("Spcific row: ", arr[1])
print("Spcific column: ", arr[:, 2])