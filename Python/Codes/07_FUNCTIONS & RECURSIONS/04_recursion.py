def factorial(n):
    if (n==1 or n==0):
        return(1)

    else:
        return(n*factorial(n-1)) # Recursion is a function which calls itself.
    
n= int(input("Enter the number: "))
print(factorial(n))