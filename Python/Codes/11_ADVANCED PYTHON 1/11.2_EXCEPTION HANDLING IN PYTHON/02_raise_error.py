a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if(b==0):
    raise ZeroDivisionError("Hey you are entering a second number 0 which is not divided by a First number in our program.")
else:
    print(a/b)