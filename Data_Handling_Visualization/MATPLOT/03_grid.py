import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Math': [85, 78, 92, 70, 88],
    'Science': [90, 76, 85, 72, 95],
    'English': [88, 82, 91, 69, 87]
}

df = pd.DataFrame(data)

plt.plot(data["Student"],data["Math"])
plt.grid()
plt.show()