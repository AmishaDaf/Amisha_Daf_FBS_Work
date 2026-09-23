# 1. Write a program to calculate area of rectangle
def Rect(l, b):
    area = l*b
    print('Area of rectangle is',area)

a = int(input('Enter Length of rectangle: '))
b = int(input('Enter breadth of rectangle: '))

Rect(a, b)