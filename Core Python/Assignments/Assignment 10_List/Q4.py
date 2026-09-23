# 4. Write a program to reverse the list.

# li = [20, 40, 10, 70, 50, 60, 30]
li = [10, 20, 30, 40, 50, 60, 70]

rev = [0] * len(li)
j = 0

for ind in range(len(li)-1 , -1, -1):
    rev[j] = li[ind]
    j = j+1
print('Original list',li)
print('Reversed list',rev)

