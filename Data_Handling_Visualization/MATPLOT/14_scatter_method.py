import matplotlib.pyplot as plt
import numpy as np

Team_A =  ([5, 12, 19, 28, 37, 31, 9, 15, 3, 24])  
Team_B =  ([6, 18, 35, 10, 7, 22, 30, 17, 13, 26])

range_score = np.array([0,5,10,15,20,25,30,35,40,45])

plt.scatter(Team_A,range_score , color = 'g')
plt.scatter(Team_B,range_score , color = 'r')

plt.xlabel("Team_A")
plt.ylabel("Team_B")

plt.title("Cricket match score")

plt.show()