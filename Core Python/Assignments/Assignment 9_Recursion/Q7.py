# 7. Write a program to find sum of digits using recursion.

def SumOfDigit(n):
    if(n <= 0):
        return 0
    else:
        d = n % 10
        return d + SumOfDigit(n//10)

n = int(input("Enter number: "))
res = SumOfDigit(n)
print('Sum of Digit is : ', res)
