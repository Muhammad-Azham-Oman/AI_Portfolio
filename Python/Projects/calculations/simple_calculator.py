print("________Simple calculator_______\n")
while True:
 print("1:Addition(+)")
 print("2:Subtraction(-)")
 print("3:Multiplication(*)")
 print("4:Division(÷)")
 print("5:Exit")

 n = int(input("Enter your choice from (1to5):"))

 if(n==5):
    print("Goodbye,see you again.")
    break

 elif(n==1):
    a = int(input("Enter the number:"))
    b = int(input("Enter the number:"))
    print(a+b)
 elif(n==2):
    a = int(input("Enter the number:"))
    b = int(input("Enter the number:"))
    print(a-b)
 elif(n==3):
    a = int(input("Enter the number:"))
    b = int(input("Enter the number:"))
    print(a*b)
 elif(n==4):
    a = int(input("Enter the number:"))
    b = int(input("Enter the number:"))
    print(a/b)

 else:
    print("Please enter a valid number to procced.")