# 6. Write a program to find print the following Fibonacci series using
# functions:
# 1 1 2 3 5 8 n terms

def Fibonacci(n):
    sum = 0
    a = -1
    b = 1
    for i in range(n+1):
        c = a + b
        sum = sum + c
        a = b
        b = c
    return sum


n = int(input('Enter number: '))
res = Fibonacci(n)
print('Sum of Fibonacci series is: ',res)
