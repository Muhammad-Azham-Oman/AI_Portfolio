import numpy as np
import time

# List
a = [1,2,3,4,5]
mul_a = (a)*2
print(mul_a)

# Numpy Array
b = np.array([1,2,3,4,5])
mul_b = (b)*2
print(mul_b)

# Efficiency of list and numpy arrays

start = time.time()
a = (i*2 for i in range(10000))
print(time.time() - start)

start = time.time()
b = np.arange(10000)*2
print(time.time()-start)