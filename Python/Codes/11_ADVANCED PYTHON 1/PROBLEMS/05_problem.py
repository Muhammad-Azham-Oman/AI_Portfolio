a = int(input("Enter the number: "))

table = [a*i for i in range(1,11)]
with open("Tables.txt","w")as f:
    f.write(str(table))