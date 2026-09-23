# 2. Write a program to check if given number is Armstrong or not using recursive
# function.

def countDigits(n):
    if n == 0:
        return 0
    else:
        return 1 + countDigits(n // 10)


def ArmstrongSum(n, digits):
    if n == 0:
        return 0
    else:
        d = n % 10
        return (d ** digits) + ArmstrongSum(n // 10, digits)


n = int(input("Enter number: "))

digits = countDigits(n)
sum = ArmstrongSum(n, digits)

if sum == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")