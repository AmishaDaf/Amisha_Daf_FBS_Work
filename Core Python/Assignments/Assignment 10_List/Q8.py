# 8. Write a program to create a duplicate of an existing list. It should not point to same list.

l1 = [10, 20, 30, 40, 50, 60, 70]
l2 = []
for ind in range(0, len(l1)):
    l2 += [l1[ind]]
print(l1)
print(l2)
print(id(l1))
print(id(l2))