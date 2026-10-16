from abc import ABC,abstractmethod
class Employee(ABC):
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

    @abstractmethod
    def calSal(self):
        pass

    def display(self):
        print(f"Id = {self.id}\t Name = {self.name}\t Sal = {self.sal}")

class Hr(Employee):
    def __init__(self, id, name, sal, com):
        super().__init__(id, name, sal)
        self.com = com
    def getCom(self):
        return self.com
    def setCom(self, ncom):
        self.com = ncom

    def calSal(self):
        print(f'Total salary : {self.sal + self.com}')

    def display(self):
        print(f'Com = {self.com}\t')
        return super().display()

class Developer(Employee):
    def __init__(self, id, name, sal, bonus):
        super().__init__(id, name, sal)
        self.bonus = bonus
    def getBonus(self):
        return self.bonus
    def setBonus(self, ncom):
        self.bonus = ncom

    def calSal(self):
        print(f'Total salary : {self.sal + self.bonus}')

    def display(self):
        print(f'Bonus = {self.bonus}\t')
        return super().display()

# e1 = Employee(10, 'Amisha', 200000)
h1 = Hr(12, 'Gauri', 150000, 2000)
d1 = Developer(14, 'Vedika', 200000, 3000)
# e1.calSal()
h1.calSal()
d1.calSal()


