class M:
    a = 1   # class variable

    def __init__(self):
        self._name = ""   # backing field
        self.fname = ""
        self.lname = ""

    @classmethod
    def b(cls):
        print(f"This is the value: {cls.a}")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        parts = value.split(" ", 1)
        if len(parts) == 2:
            self.fname, self.lname = parts
        else:
            self.fname = parts[0]
            self.lname = ""

c = M()
c.name = "Azham Oman"

print("Full Name:", c.name)
print("First Name:", c.fname)
print("Last Name:", c.lname)

# class variable access
c.b()
c.a = 34   # instance variable (different from class variable)
c.b()      # still prints class variable, not instance one
print("Instance a:", c.a)
print("Class a:", M.a)