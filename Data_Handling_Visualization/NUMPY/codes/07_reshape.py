import numpy as np

a = np.arange(0,12)
print("Originaal shape:",a)

reshaped = a.reshape((3,4))
print("Changed shape:",reshaped)

# to convert matrix or tensor into vector or flat shape

flattened = reshaped.flatten()
print("Flattened shape: ",flattened)

''' revel (return view , instead of copy) means it will show you form the original array
instaed of copy'''

reveled = reshaped.ravel()
print("Revelled: ",reveled)

# transpose maens if a is (3,4) then it change a to (4,3) means it chage the order
transposed = reshaped.T
print("Transposed: ",transposed)

# Array Compatibility

arr_1 = np.array([1,2,3])
arr_2 = np.array([4,5,6,7])
arr_3 = np.array([7,8,9])
print("Array Compatibility 1", arr_1.shape==arr_2.shape)
print("Array Compatibility 2", arr_1.shape==arr_3.shape)