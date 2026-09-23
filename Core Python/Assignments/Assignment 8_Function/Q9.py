# 9. Write a program to check if entered number is a palindrome or
# not.

def Palindrome(n):
    rev = 0
    temp = n
    while(temp > 0):
        d = temp % 10
        temp = temp // 10
        rev = rev * 10 + d
    return rev


n = int(input('Enter number : '))
res = Palindrome(n)
if(res == n):
    print('Number is Palindrome', )
else:
    print('Number is not Palindrome')

