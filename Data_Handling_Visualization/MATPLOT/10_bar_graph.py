import matplotlib.pyplot as plt
import numpy as np

Students = np.array(['Alice', 'Bob', 'Charlie', 'David', 'Eva'])
Marks = np.array([85, 78, 92, 70, 88])

plt.bar(Students,Marks)

plt.xlabel("Students")
plt.ylabel("Marks")

plt.title("MARKS SHEET")

plt.show()