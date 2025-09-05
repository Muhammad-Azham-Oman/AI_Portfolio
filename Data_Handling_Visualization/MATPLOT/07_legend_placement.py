import matplotlib.pyplot as plt
import numpy as np

a = np.arange(5)
b = [2,3,5,6,10]
c = [1,3,4,7,9]


fig = plt.figure()
ax = plt.subplot()
ax.plot(a,b,"k--",label = "Frequency")
ax.plot(a,c,"k:",label = "Period")

ax.legend(loc="center left")

plt.title("Frequency of the signal")

plt.show()

''' We can position the legend on upper,lower:right,left
We can also position it on upper,lower:center
We can position it on center:right,left'''