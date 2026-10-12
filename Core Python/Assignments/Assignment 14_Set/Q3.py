# 3. Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. 
# Use Python set data type.

s = input('Enter string: ')
b = s.split()
a = set(b)
s1 = {}
print('After converting the input into set ',a)
# word = 0
for word in b:
    if word in s1:
        s1[word] = s1[word] + 1
    else:
        s1[word] = 1
print(s1)
