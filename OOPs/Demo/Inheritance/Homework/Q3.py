class Vehicle:
    def __init__(self, vno, brand, price):
        self.vno = vno
        self.brand = brand
        self.price = price

    def getVehicle_no(self):
        return self.nvo

    def setVehicle_no(self, nvno):
        self.vno = nvno

    def getBrand(self):
        return self.brand

    def setBrand(self, nbrand):
        self.brand = nbrand

    def getPrice(self):
        return self.price

    def setPrice(self, nprice):
        self.price = nprice

    def display(self):
        print(f"Vehicle_no = {self.vno}\tBrand = {self.brand}\tPrice = {self.price}")


class Car(Vehicle):
    def __init__(self, vno, brand, price, no_of_doors):
        super().__init__(vno, brand, price)
        self.no_of_doors = no_of_doors
    def getNo_of_doors(self):
        return self.no_of_doors
    def setNo_of_doors(self, nno_of_doors):
        self.no_of_doors = nno_of_doors
    def display(self):
        print(f'No. of Doors = {self.no_of_doors}\t')
        return super().display()


class Bike(Vehicle):
    def __init__(self, vno, brand, price, engine_cc):
        super().__init__(vno, brand, price)
        self.engine_cc = engine_cc
    def getEngine_cc(self):
        return self.engine_cc
    def setEngine_cc(self, nengine_cc):
        self.engine_cc = nengine_cc
    def display(self):
        print(f'Engine CC = {self.engine_cc}\t')
        return super().display()


v1 = Vehicle(101, 'Tata', 1000000)
c1 = Car(102, 'BMW', 1800000, 4)
b1 = Bike(103, 'Mercedes', 1500000, 150)
v1.display()
c1.display()
b1.display()