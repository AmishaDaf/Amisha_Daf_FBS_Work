# 2. Write a Python program to remove the intersection of a second set with a first set.

s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}
print('Before removing intersection: ',s1)
s1.intersection(s2)
s1.remove(30)
s1.remove(40)
print('After removing intersection: ',s1)