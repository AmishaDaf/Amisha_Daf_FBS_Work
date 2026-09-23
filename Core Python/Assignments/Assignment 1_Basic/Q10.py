# 10. Write a program to calculate area of an equilateral triangle.

import math

s = int(input('Enter side of equilateral triangle: '))
area = (math.sqrt(3)/4) * s*s
print(f'Area of equilateral triangle is {area}')