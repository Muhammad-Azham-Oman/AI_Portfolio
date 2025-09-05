import random

computer = random.choice((1,0,-1))
youstr=input("Enter your choice: ")
youdict={"s":1,"w":0,"g":-1}
reversedict={1:"snake",0:"water",-1:"gun"}
you = youdict[youstr]
print(f"You chose {reversedict[you]}\nComputer chose {reversedict[computer]}")

if(computer==you):
    print("draw")

elif(computer==1,you==0):
    print("You loss!")
elif(computer==1,you==-1):
    print("You win")
elif(computer==0,you==1):
    print("You win")
elif(computer==0,you==-1):
    print("You win")
elif(computer==-1,you==0):
    print("You loss!")
elif(computer==-1,you==1):
    print("You loss!")

else:
    print("Something went wrong")