from Person import Person

class Employee(Person):
    def __init__(self, firstName, lastName, department):
        super().__init__(firstName, lastName)
        self.department = department
    
    def printInfo(self):
        print(f"{self.firstName} {self.lastName} is belongs to {self.department} department")

e1 = Employee("Arun", "Jain", "IT")

e1.printInfo()