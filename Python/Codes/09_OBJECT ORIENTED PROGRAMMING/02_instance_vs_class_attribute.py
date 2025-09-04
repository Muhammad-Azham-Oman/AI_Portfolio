n = input("Enter your name: ")
class Employee():
    name = n
    language = "python" #this is class attribute
    salary = "1000000"

Azham = Employee()
Azham.language = "Java" #this is instance attribute
print(Azham.name,Azham.language,Azham.salary)

Arham = Employee()
print(Arham.name,Arham.language,Arham.salary)