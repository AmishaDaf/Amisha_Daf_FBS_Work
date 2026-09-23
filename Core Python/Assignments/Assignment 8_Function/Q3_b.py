# 3. Write a program to find sum of following series using functions :
# b. 1!+ 2! + 3! + 4!+..... + n!

def Series(n):
    fact = 1
    sum = 0
    for i in range(1, n+1):
        
        fact = fact * i
        sum = sum + fact
    return sum


n = int(input('Enter range: '))
res = Series(n)
print('Sum of series is: ',res)


