n = input("Enter your name: ")
class Employee():
    name = n
    language = "py" #this is class attribute
    salary = "1000000"
    
    def __init__(self):
          print("Hello")

    def Employee(self):
        print(f"{self.name} has the {self.language}\nand {self.salary}")
    @staticmethod
    def greet():
        print("Good Morning")

Azham = Employee()
Azham.language = "Java" #this is instance attribute
print(Azham.name,Azham.language,Azham.salary)

Employee.greet()
Employee.Employee(Azham)