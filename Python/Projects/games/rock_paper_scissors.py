import random
print("________WELCOME________\n")
print("Choose 'r' for 'Rock'")
print("Choose 'p' for 'Paper'")
print("Choose 's' for 'Scissors'")
print("Choose 'e' for 'Exit'")

while True:
    computer = random.choice(["r","p","s"])
    n = input("Enter your choice:")
    if(n=="e"):
        print("Goodbye,see you soon")
        break
    if(computer==n):
        print("Draw")
        print(f"You choose:{n}\nComputer choose:{computer}")
    elif (computer=="r" and n=="s"):
        print("You lose!")
        print(f"You choose:{n}\nComputer choose:{computer}")
    elif(computer=="r" and n=="p"):
        print("You win!")
        print(f"You choose:{n}\nComputer choose:{computer}")
    elif(computer=="p" and n=="s"):
        print("You win!")
        print(f"You choose:{n}\nComputer choose:{computer}")
    elif(computer=="p" and n=="r"):
        print("You lose!")
        print(f"You choose:{n}\nComputer choose:{computer}")
    elif(computer=="s" and n=="p"):
        print("You lose!")
        print(f"You choose:{n}\nComputer choose:{computer}")
    elif(computer=="s" and n=="r"):
        print("You win!") 
        print(f"You choose:{n}\nComputer choose:{computer}")
    else:
     print("Something went wrong.")

 