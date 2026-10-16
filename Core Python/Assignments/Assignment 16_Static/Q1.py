# Create a class Book with members as bid,bname,price and author.Add following methods:  
# a. Constructor (Support both parameterized and parameterless)  
# b. Destructor   
# c. ShowBook  
# d. Add static variable count and also maintain count of objects created.

class Book:
    count = 0
    def __init__(self, bid = 1234, bname = "LoveGuru", price = 500, author = 'Vedika'):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count += 1

    def getBid(self):
        return self.bid
    def setBid(self, nbid):
        self.bid = nbid

    def getBname(self):
        return self.bname
    def setBname(self, nbname):
        self.bname = nbname

    def getPrice(self):
        return self.price
    def setPrice(self, nprice):
        self.price = nprice

    def getAuthor(self):
        return self.author
    def setAuthor(self, nauthor):
        self.author = nauthor

    def __del__(self):
        print('Destructor')
        Book.count -=1
        print(Book.count)               # Optional

    def showBook(self):
        print(f'BookId = {self.bid}\t BookName = {self.bname}\t Price = {self.price}\t Author = {self.author}\t Book count = {Book.count}')

b1 = Book(1, 'Life', 1000, 'Amisha')
b1.showBook()
b2 = Book()
b2.showBook()
b3 = Book(5, 'Life', 1000, 'Amisha')
b4 = Book(2, 'Life', 1000, 'Amisha')
b5 = Book(3, 'Life', 1000, 'Amisha')
print(Book.count)
    