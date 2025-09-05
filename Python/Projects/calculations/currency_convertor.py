print("Click '1' to convert rupees to Dollars.")
print("Click '2' to convert rupees to Euros.")
print("Click '3' to convert rupees to Dirhams.")
print("Click '4' to convert rupees to Dinnar.")
print("Click '5' to exit.")

while True:
 try:
    n = int(input("Enter the number from (1to5) :"))
    if(n==5):
        print("Goodbye,see you soon")
        break

    elif(n==1):
        a = int(input("Enter your money in ruppees."))
        print(f"${a*0.0035}")

    elif(n==2):
        a = int(input("Enter the number:"))
        print(f"€{a*0.0031}")

    elif(n==3):
        a = int(input("Enter the number:"))
        print(f"AED {a*0.0129}")

    elif(n==4):
        a = int(input("Enter the number:"))
        print(f"KWD {a*0.00108}")

 except ValueError:
   print("Invalid number")