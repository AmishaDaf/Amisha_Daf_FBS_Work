# 2. Python Program to Merge Two Lists and Sort it

l1 = [3, 5, 4, 2, 1]
l2 = [9, 10, 6, 8, 7]


print('Original list 1: ',l1)
print('Original list 2: ',l2)
l1.extend(l2)
print('After merge list 1 and list 2',l1)
l1.sort()
print('After sorting list: ',l1)


