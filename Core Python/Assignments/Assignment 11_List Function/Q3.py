# 3. Python Program to Sort the List According to the Second Element in Sublist

l1 = [[1, 30], [5, 10], [3, 20], [4, 40]]
l1.sort(key = lambda x : x[1])
print(l1)