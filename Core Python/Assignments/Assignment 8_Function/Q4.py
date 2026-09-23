# 4. Sum of all odd numbers between 1 to n

def sumOfOdd(n):
    sum = 0
    for i in range(1, n+1):
        if(i % 2 != 0):
            sum = sum + i
    return sum

num = int(input('Enter number: '))
res = sumOfOdd(num)
print('Sum of odd number is: ',res)
