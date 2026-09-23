# 8. Write a program to check whether a number is prime or not using recursion.

def prime(n, i):
    if(n <= 1):
        return False
    elif(i == n):
        return True
    elif(n % i == 0):
        return False
    else:
        return prime(n, i + 1)


n = int(input("Enter a number: "))
res = prime(n, 2)

if(res):
    print("Number is Prime")
else:
    print("Number is not Prime")