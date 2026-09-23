# 12. Write a program to check if given 3 digit number is a palindrome or not.

n = int(input('Enter number: '))
temp = n
rev = 0

d1 = temp % 10
temp = temp // 10
print(d1)

d2 = temp % 10
temp = temp // 10
print(d2)

d3 = temp % 10
temp = temp // 10
print(d3)

if(d1 == d3):
    print('Number is palindrome')
else:
    print('Number is not palindrome')