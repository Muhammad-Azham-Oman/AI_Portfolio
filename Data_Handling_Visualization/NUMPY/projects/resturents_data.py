import numpy as np

data = np.array([
 [1200, 1500, 1300, 1250, 1600, 1550, 1700, 1650, 1600, 1750, 1800, 1900],  # Bella Pasta
 [1000, 1100, 1200, 1050, 1300, 1250, 1400, 1350, 1200, 1450, 1500, 1550],  # Urban Tandoor
 [1800, 1750, 1850, 1900, 1950, 2000, 2100, 2200, 2150, 2250, 2300, 2400],  # Sushi Zen
 [ 900,  950, 1000,  980, 1050, 1100, 1150, 1200, 1180, 1250, 1300, 1350],  # Grill Master
 [1500, 1550, 1600, 1580, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000],  # The Greek Bowl
 [ 800,  850,  900,  880,  950,  980, 1000, 1020, 1050, 1100, 1150, 1200],  # Taco Fiesta
 [1400, 1450, 1500, 1480, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900],  # Curry Junction
 [1300, 1350, 1400, 1380, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800],  # Fusion Flavors
 [1100, 1150, 1200, 1180, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600],  # Vegan Delight
 [ 950, 1000, 1050, 1030, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450]   # Burger Spot
])

print(data.shape)
b = data.shape[0]
a = data.shape[1]
print(f"The number of resturents are: {b} and there are {a} mounths of profit.")

april_profit = data[2,3]
print("The profit of Sushi Zen resturent in apirl is ",april_profit)

july_sept_profit = np.sum(data[5,6:9])
print("The profit of Taco Fiesta resturent from july to september is ",july_sept_profit)

all_sept_profit = np.sum(data[:,8])
print("The profit of all resturents in september is ",all_sept_profit)

year_fusion_profit = np.sum(data[7,:])
print("The profit of Fusion Flavour of year is ",year_fusion_profit)

print(data.sum())

march_profit = data[:,2]
print(np.sum(march_profit))

print(data[2,11])


a = data[:,11].argmax()
print(a)

diff = data[:, 11] - data[:, 0]
print(diff)

data_1to3 = data[:3,:]
print("\nData of first 3 resturents are:\n",data_1to3)

print("\nTotal sales per month:\n",np.sum(data,axis=0))

print("\nTotal sales per month of all resturents\n:",np.sum(data[:]))

print("\nMinimum sales per resturent\n:",np.min(data,axis=1))

print("\nMaximum sales per month:\n",np.max(data,axis=0))

print("\nAverage sale per resturent in all months:\n",np.round(np.mean(data,axis=1),2))

print("\nCumulative sales pre month of each resturent:\n",np.cumsum(data,axis=1))