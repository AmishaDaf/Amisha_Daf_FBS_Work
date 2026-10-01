# 10. Write a program to remove all occurrences of a given element in the list. 

l1 = [10, 20, 30, 40, 50, 30, 70, 80, 90]
l2 = []
n = int(input('Enter element to remove from list: '))
for ind in range(0, len(l1)):
    if(l1[ind] == n):
        continue
    l2 += [l1[ind]]
print('Existing list: ',l1)
print('New list: ',l2)
