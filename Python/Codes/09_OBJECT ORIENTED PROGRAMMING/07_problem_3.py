import random
from random import randint
class Train:
    trainNo = 101123
    def __init__(self):
        print("Hello")
    def trainno(self):
        print(f"The train number {self.trainNo} is here.")
    def trainstatus(self):
        print("The train is ariving soon.")
    def trainfare(self):
        print(f"The train has fare {randint(1000,5000)}.")

t = Train()
t.trainNo = 101254
Train.trainno(t)
Train.trainstatus(t)
Train.trainfare(t)