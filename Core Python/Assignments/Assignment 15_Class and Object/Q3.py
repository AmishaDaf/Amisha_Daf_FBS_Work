# Create a class Shirt  with members as sid,sname,type(formal etc), price and size(small,large etc) .Add following methods:    
# g. Constructor (Support both parameterized and parameterless)  
# h. Destructor
# i. ShowBook

class Shirt:
    def __init__(self, sid=101, sname="Cotton Shirt", type="Formal", price=800, size="Large"):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def ShowBook(self):
        print(f"Shirt ID = {self.sid}\t Shirt Name = {self.sname}\t Type = {self.type}\t Price = {self.price}\t Size = {self.size}")

    def __del__(self):
        print("Shirt object destroyed")


# Parameterless constructor
s1 = Shirt()
s1.ShowBook()
# Parameterized constructor
s2 = Shirt(102, "Denim Shirt", "Casual", 1200, "Small")
s2.ShowBook()