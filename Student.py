from Person import Person

class Student(Person):
    def __init__(self, firstName, lastName, course):
        super().__init__(firstName, lastName)
        self.course = course

    def printInfo(self):
        print(f"{self.firstName} {self.lastName} belongs to {self.course}")

s1 = Student("Arun", "Jain", "BCA")

s1.printInfo()