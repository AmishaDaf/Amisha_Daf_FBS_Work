# 3. Python Program to Detect if Two Strings are Anagrams
str1 = input('Enter string 1: ')
str2 = (input('Enter string 2: '))

a = sorted(str1)
b = sorted(str2)
print(a)
print(b)

if(a == b):
    print("String is an Anagram")
else:
    print('String is not an Anagram')