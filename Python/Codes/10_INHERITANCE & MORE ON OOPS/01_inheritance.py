class programmer():
    name = "Azham"
    def __init__(self):
        print("Hello")
    def showname(self):
        print(f"The name of a user is {self.name}.")

class coder(programmer):
    language = "python"
    def showlanguage(self):
        print(f"The language is {self.language}.")

a = programmer()
b = coder()
b.showlanguage()
b.showname()