import random
c = random.randint(1,100)
print("_______WELCOME______\n")
attempt = 0

while True:
  try:
    n=int(input("Enter the number from (1to100):"))
    attempt += 1
    if (1>n or n>100):
        print("You entered a invalid number.")
        continue
    elif(c<n):
        print("Lower number please!")
    elif(c>n):
        print("Higher number please!")
    elif(c==n):
        print(f"Congratulations,you choose the perfect number in {attempt} attempts.")
        break
  except ValueError:
        print("You don't entered a number.")