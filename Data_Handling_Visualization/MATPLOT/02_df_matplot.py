import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Name": [
        "Emma Wilson", "Liam Carter", "Olivia Turner", "Noah Bennett", "Ava Morgan",
        "Elijah Brooks", "Sophia Reed", "James Hayes", "Isabella Jenkins", "Benjamin Ross",
        "Mia Price", "Lucas Foster", "Charlotte Perry", "Logan Hughes", "Amelia Powell",
        "Mason Coleman", "Harper Howard", "Ethan Patterson", "Evelyn Bryant", "Jacob Alexander",
        "Abigail Simmons", "Michael Ward", "Emily Griffin", "Daniel Hayes", "Elizabeth Butler",
        "Matthew Myers", "Scarlett Long", "Henry Kennedy", "Aria Barnes", "Jackson Lane",
        "Lily Palmer", "Sebastian Owens", "Chloe Gordon", "Aiden Watts", "Ella Wallace",
        "Samuel Duncan", "Grace Hopkins", "David Hart", "Victoria Fox", "Carter Matthews",
        "Penelope Barker", "Wyatt Cross", "Layla Stevenson", "Julian Morris", "Nora Day",
        "Gabriel Wheeler", "Zoey Richards", "Levi Lawson", "Hannah Stone", "Isaac Fisher"
    ],
    "Designation": [
        "Senior", "Junior", "Head", "Inter", "Junior",
        "Head", "Senior", "Inter", "Senior", "Junior",
        "Head", "Inter", "Junior", "Senior", "Head",
        "Inter", "Junior", "Senior", "Head", "Inter",
        "Junior", "Head", "Senior", "Inter", "Head",
        "Junior", "Senior", "Inter", "Head", "Junior",
        "Senior", "Inter", "Head", "Junior", "Senior",
        "Inter", "Junior", "Senior", "Head", "Inter",
        "Junior", "Head", "Senior", "Junior", "Head",
        "Inter", "Senior", "Junior", "Inter", "Head"
    ]
}

df = pd.DataFrame(data)
plt.plot(df["Name"],df["Designation"])
plt.show()

data_1 = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Math': [85, 78, 92, 70, 88],
    'Science': [90, 76, 85, 72, 95],
    'English': [88, 82, 91, 69, 87]
}

dataframe = pd.DataFrame(data_1)
plt.plot(dataframe["Student"],dataframe["Science"])
plt.show()