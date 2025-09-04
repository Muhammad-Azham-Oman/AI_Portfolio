def greatest(a,b,c):
    if(a>b and a>c):
        return(a)

    elif(b>a and b>c):
        return(b)

    elif(c>a and c>b):
        return(c)

num1 = 1
num2 = 2
num3 = 3

print(greatest(num1,num2,num3))