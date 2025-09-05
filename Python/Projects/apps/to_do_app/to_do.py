print("______WELCOME_____\n        📋")

print("Clik'1'to add tasks.")
print("Clik'2'to view tasks.")
print("Clik'3'to mark tasks as done.")
print("Clik'4'to delete tasks.")
print("Clik'5'to exit app.")

try:
 while True:
   n = int(input("Enter the number from (1to5):"))

   if(n==5):
    print("Goodbye,see you soon.")
    break

   elif(n==1):
    a = input("Enter the task:")
    with open("to_do.txt","a") as f:
        f.write(f"\n{a}")

   elif(n==2):
    with open("to_do.txt","r") as f:
     content = f.readlines()
     print(content)
        
   elif(n==3):
    with open("to_do.txt","a") as f:
        f.write("Done")

   elif(n==4):
    with open("to_do.txt","w") as f:
       f.write(" ")
except ValueError:
  print("Invalid number.")