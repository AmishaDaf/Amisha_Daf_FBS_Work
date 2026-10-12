# 10. Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions
s1 = input('Enter string 1: ')
s2 = input('Enter string 2: ')
l1 = len(s1)
l2 = len(s2)
if(s1 > s2):
    print('String 1 is larger')
elif(s2 > s1):
    print('String 2 is larger')
else:
    print('String 1 and String 2 are equal')