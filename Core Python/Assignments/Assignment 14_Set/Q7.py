# 7. Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa. 
# Use the Python set.

s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}
print('Missing number in first set is ',s2.difference(s1))
print('Missing number in second set is ',s1.difference(s2))