class programmer():
    def __init__(self):
        print("You are a programmer")
    name = "Azham"
    def showname(self):
        print(f"The name of a user is: {self.name}.")

class coder(programmer):
    def __init__(self):
        super().__init__()
        print("You are a coder")
    language = "python"
    def showlanguage(self):
        print(f"The language he knows is: {self.language}.")

class child(coder):
    def __init__(self):
        super().__init__()
        print("You are a child")
    company = "BLS"
    def showcompany(self):
        print(f"The company he is working in is: {self.company}.")

c = child()
c.showname()
c.showlanguage()
c.showcompany()