class Student:
    inName = 'FBS'
    @staticmethod
    def setInName(niname):
        Student.inName=niname

    def __init__(self, frn, name, bname):
        self.frn = frn
        self.name = name
        self.bname = bname

    def display(self):
        print(f"FRN = {self.frn}\t Name = {self.name}\t Batch_name = {self.bname}\t Instute_name = {self.inName}")

# s1 = Student(10, 'Amisha', 'July-Aug')
# s2 = Student(12, 'Gauri', 'Aug')
# s3 = Student(13, 'Sanvi', 'Sep')
# s1.display()
# s2.display()
# s3.display()

# print(Student.inName)
# s1.setInName('Firstbit Solution')
print(Student.inName)
Student.setInName('Firstbit Solution')              # Without creating object we can call static method
print(Student.inName)


