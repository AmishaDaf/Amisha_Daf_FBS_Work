# 15.  Python Program to find larger string without using built-in functions.

s1 = input('Enter string 1: ')
s2 = input('Enter string 2: ')
c1 = 0
c2 = 0
for i in s1:
    c1 += 1
for j in s2:
    c2 += 1

if(c1 > c2):
    print(f'String 1 {s1} is larger')
elif(c2 > c1):
    print(f'String 2 {s2} is larger')
else:
    print(f'Both string are equal')