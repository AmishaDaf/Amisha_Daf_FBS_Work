class File:
    def __init__(self, size, name1, format):
        self.size = size
        self.name = name1
        self.format = format

    def getSize(self):
        return self.size
    def setSize(self, newsize):
        self.size = newsize

    def getName(self):
        return self.name
    def setName(self, newname):
        self.name = newname

    def getFormat(self):
        return self.format
    def setFormat(self, newformat):
        self.format = newformat

    def display(self):
        print(f"Size = {self.size}\t Name = {self.name}\t Format = {self.format}")

e1 = File(101, 'Amisha_Images', 'jpeg')
e2 = File(120, 'Gauri_Images', 'jpeg')
print(e1.getName())
e1.display()
e2.display()
e2.setSize(190)
e2.display()