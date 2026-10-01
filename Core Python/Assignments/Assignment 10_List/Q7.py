# 7. Write a program to create a new list from existing list which contains cube of each number of list.

l1 = [2, 3, 4, 5, 6]
l2 = []
# j = 0
for ind in range(0, len(l1)):
    l2 += [l1[ind] ** 3]
    
print(l1)
print(l2)