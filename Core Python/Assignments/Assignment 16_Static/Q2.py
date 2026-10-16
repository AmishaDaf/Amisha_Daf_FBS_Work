# Create a class Product with members as pid,pname,price and quantity .Add following methods:  
# e. Constructor (Support both parameterized and parameterless)  
# f. Destructor   
# g. ShowBook  
# h. Add static member discount.  
# i. Provide methods for applying discount on price of product.

class Product:
    discount = (10/100)
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
        print(f'ProductId = {self.pid}\t Product Name = {self.pname}\t Price = {self.price}\t Quantity = {self.quantity}\t Discount = {self.price * self.discount}')

    def tPrice(self):
        print(f'Total Price = {self.price - (self.price * self.discount)}')

    def __del__(self):
        print("Product object destroyed")


# Parameterless constructor
p1 = Product()
p1.ShowBook()
p1.tPrice()
# Parameterized constructor
p2 = Product(102, "Laptop", 50000, 1)
p2.ShowBook()
p2.tPrice()