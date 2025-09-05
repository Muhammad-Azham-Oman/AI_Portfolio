o = int(input("Enter the year you were born:"))
c = 2025
if(o>c):
    print("You can't born in future.")
else:
    age = c-o
print(f"You are {age} years old.")