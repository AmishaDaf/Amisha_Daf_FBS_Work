# 6. Python Program to Multiply All the Items in a Dictionary

d = {'a': 10, 'b': 20, 'c': 30}
product = 1
for i in d.values():
    product *= i
print('Multiplication of all items is: ',product)
