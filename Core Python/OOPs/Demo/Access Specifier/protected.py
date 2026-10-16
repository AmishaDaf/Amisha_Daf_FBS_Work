class Employee:
    def __init__(self, id, name, sal):        
        self._id = id
        self._name = name
        self._sal = sal

    def getId(self):
        return self._id
    def setId(self, newid):
        self._id = newid

    def __str__(self):
        return f"Id = {self._id}\t Name = {self._name}\t Sal = {self._sal}"

class Hr(Employee):
    def __str__(self):
        print(self._id)
        return super().__str__()
e1 = Employee(1, 'Amisha', 123455)
print(e1)
print(e1.getId())
e1.setId(19)
print(e1.getId())
h1 = Hr(2, 'Gauri', 125670)
print(h1.getId())
print(h1)

    