# 8. Python Program to Remove the Characters of Odd Index Values in a String 

str = input('Enter string: ')
r = ' '
for i in range(0, len(str)):
    if(i % 2 == 0):
        r += str[i]
print(r)