# 10. Write a program to reverse three-digit number.

num = int(input('Enter number: '))

d1 = num % 10
n1 = num // 10
print(d1)

d2 = n1 % 10
n2 = n1 // 10
print(d2)

d3 = n2 % 10
n3 = n2 // 10
print(d3)

print(f'Reverse of {num} is {d1}{d2}{d3}')