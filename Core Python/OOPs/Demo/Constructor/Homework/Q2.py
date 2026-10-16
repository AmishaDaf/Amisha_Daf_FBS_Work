class Product:
    def __init__(self, id1, name1, price1):
        self.id = id1
        self.name = name1
        self.price = price1

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

e1 = Product(101, 'Sunscreen', 600)
e2 = Product(102, 'Moisturizer', 200)
print(e1.getName())
e1.display()
e2.display()
e2.setPrice(230)
e2.display()