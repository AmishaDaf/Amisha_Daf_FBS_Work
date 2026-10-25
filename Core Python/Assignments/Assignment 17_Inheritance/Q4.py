# Create a derived class from Student as EnggStudent with : 
# a. Data   members as :  
#     i. Branch
#     ii. InternalMarks
# b. Add the following methods : 
#     i. Parameterized constructor 
#     ii. Display
#     iii. Accept
#     iv. override Method CalculateRank 
#     v. Override __str__ Method 

class Student:
    def __init__(self, id = None, name = None, age = None, per = None):
        self.id = id
        self.name = name
        self.age = age
        self.per = per

    def Display(self):
        print(f"Student ID: {self.id}\t Name: {self.name}\tAge: {self.age}\tPercentage: {self.per}")

    def Accept(self):
        self.id = int(input("Enter Student ID: "))
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.per = float(input("Enter Percentage: "))


    def CalculateRank(self):
        if self.per >= 75:
            return "Distinction"
        elif self.per >= 60:
            return "First Class"
        elif self.per >= 40:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Percentage: {self.per}"


class EnggStudent(Student):
    def __init__(self, id = None, name = None, age = None, per = None, branch = None, imarks = None):
        super().__init__(id, name, age, per)
        self.branch = branch
        self.imarks = imarks

    def Display(self):
        super().Display()
        print(f"Branch: {self.branch}\t Int Marks: {self.imarks}")

    def Accept(self):
        super().Accept()
        self.branch = input('Enter Branch: ')
        self.imarks = int(input('Enter Internal Marks: '))

    def CalculateRank(self):
        return super().CalculateRank()

    def __str__(self):
        return f"{super().__str__()}, Branch: {self.branch}, Internal Marks: {self.imarks}"


s1 = EnggStudent()
s1.Accept()
s1.Display()
print("Result:", s1.CalculateRank())
print(s1)

