# Create a class Complex Number with data members as real and imag and add following methods : 
# a. Constructor 
# b. Destructor 
# c. Overload +,-  operator

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    
    def __str__(self):
        return f'{self.real} + {self.imag}i'

    def __add__(self, other):
        r = self.real + other.real
        i = self.imag + other.imag
        return ComplexNumber(r, i)

    def __sub__(self, other):
        r = self.real - other.real
        i = self.imag - other.imag
        return ComplexNumber(r, i)

    def __del__(self):
        print("Object destroyed")
    
x = ComplexNumber(5, 6)
y = ComplexNumber(4, 5)

print("Addition:", x + y)
print("Subtraction:", x - y)