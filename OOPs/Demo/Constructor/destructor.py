class Employee:
    def __init__(self, id1, name1, sal1):
        self.id = id1
        self.name = name1
        self.sal = sal1

    def getId(self):
        return self.id
    def setId(self, newid):
        self.id = newid

    def getName(self):
        return self.name
    def setName(self, newname):
        self.name = newname

    def getSal(self):
        return self.sal
    def setSal(self, newid):
        self.sal = newid

    def display(self):
        print(f"Id = {self.id}\t Name = {self.name}\t Sal = {self.sal}")

    def __del__(self):
        print('I am in destructor')

e1 = Employee(10, 'Amisha', 200000)
e2 = Employee(12, 'Gauri', 150000)
print(e1.getName())
e1.display()
e2.display()
e2.setSal(190000)
e2.display()