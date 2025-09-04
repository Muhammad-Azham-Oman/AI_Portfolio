b  = int(input("Enter your total marks: "))

if(b>=90 and b<=100):
    print("A+")

elif(b>=80 and b<=90):
    print("A")
elif(b>=70 and b<=80):
    print("B")
elif(b>=60 and b<=70):
    print("C")
elif(b>=50 and b<=60):
    print("D")
elif(b>=0 and b<50):
    print("F")

else:
    print("You Entered the invalid numbers")