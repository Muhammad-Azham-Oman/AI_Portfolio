# Method 1


import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Math': [85, 78, 92, 70, 88],
    'Science': [90, 76, 85, 72, 95],
    'English': [88, 82, 91, 69, 87]
}

df = pd.DataFrame(data)
plt.plot(data['Student'],data['English'])
plt.xlabel("Student(Names)")
plt.ylabel("English(Marks)")

# for placement in Center
plt.title("Marks Sheet")

plt.grid()
plt.show()


# Method 2


import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Math': [85, 78, 92, 70, 88],
    'Science': [90, 76, 85, 72, 95],
    'English': [88, 82, 91, 69, 87]
}

df = pd.DataFrame(data)
plt.plot(data['Student'],data['English'])
plt.xlabel("Student(Names)")
plt.ylabel("English(Marks)")

# for placement in Right
plt.title("Marks Sheet",loc="right")

plt.grid()
plt.show()


# Method 3


import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Math': [85, 78, 92, 70, 88],
    'Science': [90, 76, 85, 72, 95],
    'English': [88, 82, 91, 69, 87]
}

df = pd.DataFrame(data)
plt.plot(data['Student'],data['English'])
plt.xlabel("Student(Names)")
plt.ylabel("English(Marks)")

# for placement in Left
plt.title("Marks Sheet",loc="left")

plt.grid()
plt.show()