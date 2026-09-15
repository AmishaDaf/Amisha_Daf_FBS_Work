# 5. Write a program to print prime numbers between 1 to 100.

n = int(input('Enter number: '))
for num in range(2, n+1):
    for i in range(2, num):
        if(num % i == 0):
            break
    else:
        print(num, end = ' ')
