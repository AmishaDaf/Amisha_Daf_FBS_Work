# 1. Write a program to find sum of following series using recursive functions:

# i. 1! + 2! + 3! + 4! +..... + n!
# Note : For fact and sum two recursive functions


def fact(n):
    if(n == 1):
        return 1
    else: 
        return n * fact(n-1) 

def SumOfSeries(n):
    if(n == 1):
        return fact(1)
    else:
        return fact(n) + SumOfSeries(n-1)

n = int(input('Enter number: '))
res = SumOfSeries(n)
print('Sum of Series is: ',res)