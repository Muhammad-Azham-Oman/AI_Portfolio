class programmer():
    name = "Azham"
    def showname(self):
        print(f"The name of a user is: {self.name}.")

class coder(programmer):
    language = "python"
    def showlanguage(self):
        print(f"The language he knows is: {self.language}.")

class chlid(coder):
    company = "BLS"
    def showcompany(self):
        print(f"The company he is working in is: {self.company}.")

a = programmer()
b = coder()
c = chlid()
c.showname()
c.showlanguage()
c.showcompany()
print(a.name)