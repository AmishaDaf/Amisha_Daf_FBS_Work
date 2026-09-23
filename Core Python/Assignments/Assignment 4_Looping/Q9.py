# 9. WAP to print all numbers in a range divisible by a given number.


r = int(input('Enter range: '))
n = int(input('Enter number you want to check within given range: '))

for i in range(1, r):
    if(i % n == 0):
        print(i)
    i += 1

