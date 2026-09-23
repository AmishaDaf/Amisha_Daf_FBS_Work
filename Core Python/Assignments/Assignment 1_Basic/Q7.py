# 7. Program to Find the Roots of a Quadratic Equation

import math
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

d = b*b - 4*a*c

r1 = (-b + math.sqrt(d)) / (2*a)
r2 = (-b - math.sqrt(a)) / (2*a)

print(f'Root 1 is : {r1} and Root 2 is : {r2}')

