a = int(input("Enter the number: "))
b = int(input("Enter the number: "))

if (b==0):
    raise ZeroDivisionError("You entered zero which cannot be in divide in our program.")
else:
    print(a/b)