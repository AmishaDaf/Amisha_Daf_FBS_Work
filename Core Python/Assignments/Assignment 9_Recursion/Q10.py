# 10. Write a program to reverse a number using recursion.
def reverse(n, rev):
    if n == 0:
        return rev
    else:
        digit = n % 10
        rev = rev * 10 + digit
        return reverse(n // 10, rev)


n = int(input("Enter number: "))

result = reverse(n, 0)

print("Reverse number =", result)