import numpy

# 0-D Array
a = numpy.array(34)
print(a)

# 1-D Array
b = numpy.array([1,2,3,4,5])
print(b)

# 2-D Array
c = numpy.array([[1,2,3,4],[5,6,7,8]])
print(c)

# 3-D Array
d = numpy.array([[[1,2,3,4],[5,6,7,8]],[[1,2,3,4],[5,6,7,8]]])
print(d)

# to see the dimention of numpy arrays
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# to change the dimention of array
e = numpy.array([1,2,3,4,5],ndmin=5)
print(e)