import matplotlib.pyplot as plt
import numpy as np

months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
rainfall = np.array([78, 60, 85, 92, 110, 140, 160, 150, 120, 95, 80, 70])

plt.plot(months,rainfall)

plt.xlabel("Months")
plt.ylabel("Rainfall")

plt.title("Rainfall perivious year in mm")

plt.show()