# 6. Python Program to Find the Union of two Lists 

l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]
l3 = []

l3 = l1
l3.extend(l2)
# print(l3)
l3 = list(set(l3))
print('Union: ',l3)

