import math
n = int(input("Enter the number: "))
sqrt = math.sqrt(n)
class calculator():
    square = n*n
    cube = n*n*n
    squareroot = (sqrt)

    @staticmethod
    def greet():
        print("Hello")

c = calculator()
calculator.greet()
print(c.square,c.cube,c.squareroot)