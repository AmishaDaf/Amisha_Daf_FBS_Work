# Create a class Book with members as bid,bname,price and author.Add following methods:  
# a. Constructor (Support both parameterized and parameterless)  
# b. Destructor   
# c. ShowBook  
class Book:
    def __init__(self, bid = 1234, bname = "LoveGuru", price = 500, author = 'Vedika'):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

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

    def showBook(self):
        print(f'BookId = {self.bid}\t BookName = {self.bname}\t Price = {self.price}\t Author = {self.author}')

b1 = Book(1, 'Life', 1000, 'Amisha')
b1.showBook()
b2 = Book()
b2.showBook()
    