# 12.  Python Program to count number of lowercase characters in a string. 

s = input('Enter string: ')
c = 0
for i in range(0, len(s)):
    if s[i].islower():
        c += 1
print(c)