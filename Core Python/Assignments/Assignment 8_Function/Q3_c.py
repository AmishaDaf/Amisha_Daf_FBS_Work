# 3. Write a program to find sum of following series using functions :
# c. 1^1 + 2^2 + 3^3+ ...... n^n


def Series(n):
    sum = 0
    num = 0
    for i in range(1, n+1):
        num = num + (i ** i)
    sum = sum + num
    return sum


n = int(input('Enter Range: '))
res = Series(n)
print('Sum of series is: ',res)

