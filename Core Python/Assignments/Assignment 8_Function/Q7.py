# 7. Write a program to find sum of digits of a number.

def sumOfDigit(n):
    sum = 0
    temp = n
    while(temp > 0):
        d = temp % 10
        temp = temp // 10
        sum = sum + d
    return sum



n = int(input('Enter number: '))
res = sumOfDigit(n)
print('Enter number: ',res)
