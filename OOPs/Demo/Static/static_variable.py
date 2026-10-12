class Student:
    inName = 'FBS'
    def __init__(self,frn,name,bname):
        self.frn = frn
        self.name = name
        self.batch = bname

    def display(self):
        print(f'FRN = {self.frn}\tName = {self.name}\tBatch_name = {self.batch}\tInst_Name = {self.inName}')


s1 = Student(12, 'Amisha', 'Aug')
s2 = Student(13, 'Gauri', 'Sep')
s3 = Student(14, 'Sanvi', 'Oct')
s1.display()
print(Student.inName)                                                   # Using class name  
print(s1.inName)                  # print above inName i.e   FBS           #Using object name
s2.display()
s3.display()

Student.inName = 'Firstbit Solution'            # FRN = 14        Name = Sanvi    Batch_name = Oct        Inst_Name = Firstbit Solution
                                                # Change the above static variable value
                                                # Line 20 Access directly but we can access it using getter and setter so we use static method for it
s3.display()
