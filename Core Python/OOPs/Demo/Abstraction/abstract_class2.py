from abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self, cNo, color):
        self.cNo = cNo
        self.color = color
    def getCno(self):
        return self.cNo
    def setCno(self,ncNo):
        self.cNo = ncNo
    def getColor(self):
        return self.color
    def setColor(self, ncolor):
        self.color = ncolor

    @abstractmethod
    def brake(self):
        pass
    def __str__(self):
        return f'C_No = {self.cNo}\t Color = {self.color}'

# v = Vehicle(11, 'Black')
# print()


class Car(Vehicle):
    def brake(self):
        print('This is the Brake of car')

c = Car(11, 'White')
print(c)
c.brake()

