class Employee():
    salary = 120
    increment = 20
    @property
    def salaryafterincrement(self):
        return (self.salary+(self.salary*self.increment/100))
    @salaryafterincrement.setter
    def salaryafterincrement(self,salary):
        self.increment = ((salary/self.salary)-1)*100


c = Employee()
print(c.salaryafterincrement)
c.salaryafterincrement = 144.0
print(c.increment)