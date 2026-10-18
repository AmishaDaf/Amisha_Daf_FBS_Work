# Create a class Distance with data members as km,m and cm and add following methods : 
# a. Constructor 
# b. Destructor 
# c. Overload +,-  operator

class Distance:
    def __init__(self, km, m, cm):
        self.km = km
        self.m = m
        self.cm = cm

    def __str__(self):
        return f'{self.km}km {self.m}m {self.cm}cm'

    def __add__(self, other):
        a = self.km + other.km
        b = self.m + other.m
        c = self.cm + other.cm
        return Distance(a, b, c)

    def __add__(self, other):
        tcm = self.cm + other.cm
        em = tcm // 100
        tcm = tcm % 100
        tm = self.m + other.m + em
        ekm = tm // 1000
        tm = tm % 1000
        tkm = self.km + other.km + ekm
        return Distance(tkm, tm, tcm)
    
    def __del__(self):
        print('Object Destroyed')

d1 = Distance(2, 500, 80)
d2 = Distance(1, 600, 40)
print(d1+d2)