class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    
    def __str__(self):
        return f"{self.firstName} {self.lastName}"
    
    def printInfo(self):
        print(f"Hello {self.firstName} {self.lastName}")