# 9. Write a program to swap two numbers without using third variable.

x = int(input('Enter number 1: '))
y = int(input('Enter number 2: '))

print(f'Bafore swapping x is {x} and y is {y}')
x, y = y, x

print(f'After swapping x is {x} and y is {y}')
