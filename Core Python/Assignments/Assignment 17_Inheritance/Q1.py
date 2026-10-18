
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __del__(self):
        print("Object destroyed")


class Operations(ComplexNumber):
    def __add__(self, other):
        r = self.real + other.real
        i = self.imag + other.imag
        print(self.real, "+", self.imag, "i")
        return Operations(r, i)



    def __sub__(self, other):
        r = self.real - other.real
        i = self.imag - other.imag
        print(self.real, "-", self.imag, "i")
        return Operations(r, i)

    
        

c1 = Operations(3, 2)
c2 = Operations(4, 5)

c3 = c1 + c2
print("Addition:")
c3.display()

c4 = c1 - c2
print("Subtraction:")
c4.display()
