# Create a class Product with members as pid,pname,price and quantity .Add following methods:  
# d. Constructor (Support both parameterized and parameterless)  
# e. Destructor   
# f. ShowBook 

class Product:
    def __init__(self, pid=101, pname="Mobile", price=15000, quantity=2):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def ShowBook(self):
        # print("Product ID:", self.pid)
        # print("Product Name:", self.pname)
        # print("Price:", self.price)
        # print("Quantity:", self.quantity)
        print(f'ProductId = {self.pid}\t Product Name = {self.pname}\t Price = {self.price}\t Quantity = {self.quantity}')

    def __del__(self):
        print("Product object destroyed")


# Parameterless constructor
p1 = Product()
p1.ShowBook()
# Parameterized constructor
p2 = Product(102, "Laptop", 50000, 1)
p2.ShowBook()