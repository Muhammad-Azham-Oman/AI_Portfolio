import matplotlib.pyplot as plt
import numpy as np

Marks = np.array([57, 33, 76, 24, 92, 65, 48, 73, 99,
                  12, 38, 59, 20, 50, 71, 68, 44,42,45])

plt.hist(Marks , bins = [0,20,40,60,80,100])

plt.xlabel("Students")
plt.ylabel("Marks")

plt.title("Students marks")

plt.show()