# 11. Write a program to print all numbers which are divisible by m and n in the list

l1 = [10, 12, 15, 20, 24, 30, 40, 60]
m = int(input('Enter value for m: '))
n = int(input('Enter value for n: '))
for ind in range(0, len(l1)):
    if(l1[ind] % 2 == 0 and l1[ind] % 3 == 0):
        print(l1[ind])