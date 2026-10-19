# Create a class Student with following  
# a. data members :   
#     i. StudentId 
#     ii. Name
#     iii. Age
#     iv. Percentage
# b. Add the following methods : 
#     i. Parameterized constructor 
#     ii. Display
#     iii. Accept
#     iv. Method CalculateRank 
#     v. Override __str__ Method 

class Student:
    def __init__(self, StudentId = None, Name = None, Age = None, Percentage = None):
        self.StudentId = StudentId
        self.Name = Name
        self.Age = Age
        self.Percentage = Percentage

    def Display(self):
        print(f"Student ID: {self.StudentId}\t Name: {self.Name}\tAge: {self.Age}\tPercentage: {self.Percentage}")

    def Accept(self):
        self.StudentId = int(input("Enter Student ID: "))
        self.Name = input("Enter Name: ")
        self.Age = int(input("Enter Age: "))
        self.Percentage = float(input("Enter Percentage: "))

    def CalculateRank(self):
        if self.Percentage >= 75:
            return "Distinction"
        elif self.Percentage >= 60:
            return "First Class"
        elif self.Percentage >= 40:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return f"ID: {self.StudentId}, Name: {self.Name}, Age: {self.Age}, Percentage: {self.Percentage}"


s1 = Student()
s1.Accept()
s1.Display()
print("Result:", s1.CalculateRank())
print(s1)