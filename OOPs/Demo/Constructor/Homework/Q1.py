class Student:
    def __init__(self, rollno1, name1, dept1):
        self.rollno = rollno1
        self.name = name1
        self.dept = dept1

    def getRollno(self):
        return self.rollno
    def setRollno(self, newrollno):
        self.rollno = newrollno

    def getName(self):
        return self.name
    def setName(self, newname):
        self.name = newname

    def getDept(self):
        return self.dept
    def setDept(self, newdept):
        self.dept = newdept

    def display(self):
        print(f"Roll_no = {self.rollno}\t Name = {self.name}\t Deptartment = {self.dept}")

e1 = Student(10, 'Amisha', 'Computer')
e2 = Student(12, 'Gauri', 'IT')
print(e1.getName())
e1.display()
e2.display()
e2.setRollno(11)
e2.display()