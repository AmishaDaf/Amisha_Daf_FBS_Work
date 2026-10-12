# 13.  Python Program to count number of digits and letters in a string. 

s = input('Enter string: ')
d = 0
l = 0
for i in range(0, len(s)):
    if s[i].isdigit():
        d += 1
    if s[i].isalpha():
        l += 1

print('Digits in string is ',d)
print('Letters in string is ',l)