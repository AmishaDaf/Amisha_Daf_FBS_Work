class Electronics:
    def display(self):
        print('ENTC')

class Mechanical:
    def display(self):
        print('Mech')

class Mechatronics(Electronics, Mechanical):
    def display(self):
        print('Mechatronics')

m = Mechatronics()
m.display()

