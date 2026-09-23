# 2. Write a program to find maximum and minimum element in a list.
li = [20, 40, 10, 70, 50, 60, 30]
max = li[0]
min = li[0]
for ind in range(1, len(li)):
    if(li[ind] > max):
        max = li[ind]
    if(li[ind] < min):
        min = li[ind]
print(f'Maximum element is: {max} and minimum element is: {min}')
    