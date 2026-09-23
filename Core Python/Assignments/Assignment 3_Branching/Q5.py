# 5. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

ab = int(input('Enter side 1: '))
bc = int(input('Enter side 2: '))
ac = int(input('Enter side 3: '))

if(ab == bc == ac):
    print('Triangle is Equilateral')
elif(ab==bc or bc==ac or ab==ac):
    print('Triangle is Isosceles')
else:
    print('Triangle is Scalene')