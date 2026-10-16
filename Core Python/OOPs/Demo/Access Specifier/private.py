class Employee:
    def __init__(self, id, name, sal):        
        self.__id = id
        self.__name = name
        self.__sal = sal

    def getId(self):
        return self.__id
    def setId(self, newid):
        self.__id = newid

    def __str__(self):
        return f"Id = {self.__id}\t Name = {self.__name}\t Sal = {self.__sal}"

class Hr(Employee):
    def __str__(self):
        # print(self.__id)
        return super().__str__()
e1 = Employee(1, 'Amisha', 123455)
print(e1.getId())
e1.setId(19)
print(e1.getId())
h1 = Hr(2, 'Gauri', 125670)
print(h1.getId())
print(h1)

    