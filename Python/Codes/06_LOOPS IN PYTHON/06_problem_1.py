'''Table of specific number'''


# With for loop
a = int(input("Enter the number: "))
for b in range(1,11):
    print(f"{a}x{b} = {a*b}")


# With while loop
a = int(input("Enter the number: "))
i = 1
while(i<11):
    print(f"{a}x{i} = {a*i}")
    i+=1