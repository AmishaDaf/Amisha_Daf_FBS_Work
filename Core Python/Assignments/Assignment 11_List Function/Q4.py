# 4. Python Program to Find the Second Largest Number in a List Using Bubble Sort 

l1 = [70, 40, 60, 10, 20, 80, 30, 50]
print('List :',l1)
size = len(l1)
for i in range(1, size):
    for j in range(0, size - i):
        if(l1[j] > l1[j+1]):
            l1[j], l1[j+1] = l1[j+1], l1[j]

# print(l1)
print('Second largest element: ',l1[-2])