import numpy as np
vector_1 = np.array([[1,2,3],[4,5,6]])
vector_2 = np.array([[7,8,9],[1,2,3]])
vector_3 = np.array([1,2,3,4])
vector_4 = np.array([5,6,7,8])

print("Sum of two vectors is:\n",vector_1+vector_2)
print("Multiplication of two vectors is:\n",vector_1*vector_2)
print("Dot product of two vectors in 2-D is:\n",np.dot(vector_1,vector_2.T))
print("Dot product of two vectors in 1-D is:\n",np.dot(vector_3,vector_4))


vector = np.array(["Olive Garden", "Chipotle", "P.F. Chang's", "Cheesecake Factory"])
vectorized_upper = np.vectorize(str.upper)
print(vectorized_upper(vector))