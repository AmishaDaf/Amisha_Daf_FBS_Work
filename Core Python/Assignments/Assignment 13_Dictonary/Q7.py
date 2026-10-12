# 7. Python Program to Remove the Given Key from a Dictionary

n = int(input('Enter number: '))
d1 = {1:'A', 2:'B', 3:'C'}
d2 = {}
for i in d1:
    if(n == i):
        continue
    d2[i] = d1[i]
print(d1)
print(d2)