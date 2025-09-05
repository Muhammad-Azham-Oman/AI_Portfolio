import random
print("________Quiz Time_______\n")
print("What type of quiz you want to solve.")
print("1:Addition(+)")
print("2:Subtraction(-)")
print("3:Multiplication(*)")
print("4:Division(÷)")
print("5:Exit")
try:
 while True:
  print("Now,What type of quiz you want to solve.")

  n = int(input("Enter your choice from (1to5):"))

  if(n==5):
    print("Goodbye,see you again.")
    break

  elif(n==1):
    a = random.randint(1,10)
    b = random.randint(1,10)
    print(f"{a}+{b}")
    c = a+b
    n = int(input("Enter the number:")) 
    if(c==n):
       print("Congratulations,You won!")
    elif(c!=n):
       print(f"Unfortunatly,You entered wrong answer.\nCorrect is {c}.")
  elif(n==2):
    a = random.randint(1,10)
    b = random.randint(1,10)
    print(f"{a}-{b}")
    c = a-b
    n = int(input("Enter the number:")) 
    if(c==n):
       print("Congratulations,You won!")
    elif(c!=n):
       print(f"Unfortunatly,You entered wrong answer.\nCorrect is {c}.")
  elif(n==3):
    a = random.randint(1,10)
    b = random.randint(1,10)
    print(f"{a}*{b}")
    c = a*b
    n = int(input("Enter the number:")) 
    if(c==n):
       print("Congratulations,You won!")
    elif(c!=n):
       print(f"Unfortunatly,You entered wrong answer.\nCorrect is {c}.")
  elif(n==4):
    a = random.randint(1,100)
    b = random.randint(1,10)
    print(f"{a}÷{b}")
    c = a//b
    n = int(input("Enter the number:")) 
    if(c==n):
       print("Congratulations,You won!")
    elif(c!=n):
       print(f"Unfortunatly,You entered wrong answer.\nCorrect is {c}.")
  else:
    print("Please enter a valid number to procced.")

except ValueError:
  print("Invalid,Please enter a number.")