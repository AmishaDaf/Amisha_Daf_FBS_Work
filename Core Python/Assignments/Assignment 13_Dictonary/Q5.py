# 5. Python Program to Sum All the Items in a Dictionary

d = {'a': 10, 'b': 20, 'c': 30}
sum = 0
for i in d.values():
    sum = sum + i
print(sum)