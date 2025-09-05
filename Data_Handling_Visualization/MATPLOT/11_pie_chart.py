import matplotlib.pyplot as plt
import numpy as np

Student = np.array(['Alice', 'Bob', 'Charlie', 'David', 'Eva'])
Marks = np.array([85, 78, 92, 70, 88])

plt.pie(Marks , labels=Student , autopct="%1.2f%%")

plt.title("MARKS SHEET")

plt.show()