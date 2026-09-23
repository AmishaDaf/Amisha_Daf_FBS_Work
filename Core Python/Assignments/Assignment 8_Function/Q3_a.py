# 3. Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n


def seriesSum(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
        i += 1
    return sum


n = int(input('Enter range: '))
res = seriesSum(n)
print('Sum of series is : ',res)