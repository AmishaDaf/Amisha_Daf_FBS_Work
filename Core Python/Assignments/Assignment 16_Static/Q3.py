# Create a class Shirt  with members as sid,sname,type(formal etc), price and size(small,large etc) .Add following methods:  
# j. Constructor (Support both parameterized and parameterless)  
# k. Destructor   
# l. ShowBook
# m. For each size of shirt price should change by 10%. 
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and xlarge=1300) Use static concept.

class Shirt:
    def __init__(self, sid=101, sname="Cotton Shirt", type="Formal", price=1000, size="Large"):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def ShowBook(self):
        print(f"Shirt ID = {self.sid}\t Shirt Name = {self.sname}\t Type = {self.type}\t Size = {self.size}")
        if(self.size == 'Small'):
            print('Price =',self.price)
        elif(self.size == 'Medium'):
            print('Price =',self.price + (self.price * (10/100)))
        elif(self.size == 'Small'):
            print('Price =',self.price + (self.price * (20/100)))
        if(self.size == 'Small'):
                    print('Price =',self.price + (self.price * (10/100)))

    def __del__(self):
        print("Shirt object destroyed")


# Parameterless constructor
s1 = Shirt()
s1.ShowBook()
# Parameterized constructor
s2 = Shirt(102, "Denim Shirt", "Casual", 1200, "Small")
s2.ShowBook()