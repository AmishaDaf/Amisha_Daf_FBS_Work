# 9. Write a program to calculate the m to the power n using recursion.

def power(m, n):
    if(m <= 0):
        return 0
    elif(m == 1 or n == 0):
        return 1
    else:
        return m * power(m, n-1)

m = int(input('Enter m: '))
n = int(input('Enter n: '))
res = power(m, n)
print(res)