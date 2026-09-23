# 2. Write a program to calculate area of circle
def Circle(r):
    area = 3.14 * r * r
    return area

r = int(input('Enter radius of circle: '))

res = Circle(r)
print(f'Area of circle is: {res}')