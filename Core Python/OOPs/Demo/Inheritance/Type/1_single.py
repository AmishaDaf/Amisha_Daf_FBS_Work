class Student:
    def __init__(self, frn, name, bname):
        self.frn = frn
        self.name = name  
        self.batch = bname

    def display(self):
        print(f'FRN = {self.frn}\tName = {self.name}\tBatch = {self.batch}')
# Student ends here ............

class PlacedStudent(Student):
    def __init__(self, frn, name, bname, cName):                # super - access everything present in base class , constructor changed
        super().__init__(frn, name, bname)
        self.cName = cName

    def setCname(self, cName):
        self.cName = cName

    def getCname(self):
        return self.cName

    
    def display(self):
        print(f'CName = {self.cName}')
        super().display()


e1 = PlacedStudent(14, 'Amisha', 'Aug', 'TCS')
# e1.display()
