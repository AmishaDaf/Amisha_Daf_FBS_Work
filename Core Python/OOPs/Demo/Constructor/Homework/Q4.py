class Vehicle:
    def __init__(self, brand, number, price1):
        self.brand = brand
        self.number = number
        self.price = price1

    def getBrand(self):
        return self.brand
    def setBrand(self, newbrand):
        self.brand = newbrand

    def getNumber(self):
        return self.number
    def setNumber(self, newnnumber):
        self.number = newnnumber

    def getPrice(self):
        return self.price
    def setPrice(self, newprice):
        self.price = newprice

    def display(self):
        print(f"Brand = {self.brand}\tNumber = {self.number}\tPrice = {self.price}")

e1 = Vehicle('Mercidees', 'MS1234', 1500000)
e2 = Vehicle('BMW', 'BMW1234', 1000000)
print(e1.getBrand())
e1.display()
e2.display()
e2.setPrice(1300000)
e2.display()