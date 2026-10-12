class Product:
    def __init__(self, id1, name, price):
        self.id = id1
        self.name = name
        self.price = price

    def getId(self):
        return self.id
    def setId(self, newid):
        self.id = newid

    def getName(self):
        return self.name
    def setName(self, newname):
        self.name = newname

    def getPrice(self):
        return self.price
    def setPrice(self, newprice):
        self.price = newprice

    def display(self):
        print(f"Product_Id = {self.id}\tName = {self.name}\tPrice = {self.price}")

class Mobile(Product):
    def __init__(self, id, name, price, sCount):
        super().__init__(id, name, price)
        self.sCount = sCount
    def getScount(self):
        return self.sCount
    def setScount(self, nsCount):
        self.sCount = nsCount
    def display(self):
        print(f'Sim_Count = {self.sCount}\t')
        return super().display()


class Laptop(Product):
    def __init__(self, id, name, price, ram):
        super().__init__(id, name, price)
        self.ram = ram
    def getRam(self):
        return self.ram
    def setRam(self, nram):
        self.ram = nram
    def display(self):
        print(f'Ram = {self.ram}\t')
        return super().display()
    

p1 = Product(101, 'Sunscreen', 600)
m1 = Mobile(102, 'Realme', 20000, 2)
l1 = Laptop(102, 'Realme', 20000, 16)
p1.display()
m1.display()
l1.display()