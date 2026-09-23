# 5. Sum of all prime numbers between 1 to n

def sumOfPrime(n):
    sum = 0
    for i in range(2, n+1):
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            sum = sum + i
    return sum

n = int(input('Enter number: '))
res = sumOfPrime(n)
print('Sum of all Prime number is: ',res)
