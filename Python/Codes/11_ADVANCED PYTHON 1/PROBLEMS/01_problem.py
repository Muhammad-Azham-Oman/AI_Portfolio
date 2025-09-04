try:
    with(
    open("1.txt","r")as f1,   
    open("2.txt","r")as f2,   
    open("3.txt","r")as f3   
    ):
      print(f1.read())
      print(f2.read())
      print(f3.read())

except:
   print("No file exists.")

print("Thank you")