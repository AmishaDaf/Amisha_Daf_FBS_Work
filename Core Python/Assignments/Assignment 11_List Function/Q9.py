# 9. Write a program to create three lists of numbers, their squares and cubes

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = []
l3 = []
for ind in range(0, len(l1)):
    l2 += [l1[ind] ** 2]
    l3 += [l1[ind] ** 3]
print("Original list: ",l1)
print("Square: ",l2)
print('cube: ',l3)