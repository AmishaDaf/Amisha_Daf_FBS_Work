# Create a class MedicalStudent inherited from Student with following 
# a. Data members :
#     i. Specialization
#     ii. MarksOfInternship
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


class MedicalStudent(Student):
    def __init__(self, id = None, name = None, age = None, per = None, specialization = None, marksOFInternship = None):
        super().__init__(id, name, age, per)
        self.specialization = specialization
        self.marksOFInternship = marksOFInternship

    def Display(self):
        super().Display()
        print(f"Specialization: {self.specialization}\t Marks Of Internship: {self.marksOFInternship}")

    def Accept(self):
        super().Accept()
        self.specialization = input('Enter Specialization: ')
        self.marksOFInternship = int(input('Enter Marks Of Internship: '))

    def CalculateRank(self):
        if self.per >= 75 and self.marksOFInternship >= 75:
            return "Distinction"
        elif self.per >= 60 and self.marksOFInternship >= 60:
            return "First Class"
        elif self.per >= 40 and self.marksOFInternship >= 40:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return f"{super().__str__()}, Specialization: {self.specialization}, Marks Of Internship: {self.marksOFInternship}"


s1 = MedicalStudent()
s1.Accept()
s1.Display()
print("Result:", s1.CalculateRank())
print(s1)

