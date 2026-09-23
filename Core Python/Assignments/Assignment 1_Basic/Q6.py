# 6. Write a Program to input two angles from user and find third angle of the triangle.

a1 = int(input('Enter angle 1: '))
a2 = int(input('Enter angle 2: '))

a3 = 180 - (a1+a2)

print(f'Third angle of triangle is: {a3}')