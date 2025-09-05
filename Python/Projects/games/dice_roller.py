import random
print("Click e to exit.")
while True:
       print("To roll the dice press:'r'")
       n = input("-->")
       if(n=="e"):
            print("Goodbye")
            break
       if(n=="r"):
           c = random.randint(1,6)
           print(f"{c}")
       else:
           print("Please enter 'r' to roll.")