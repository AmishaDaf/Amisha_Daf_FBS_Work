# 10. Write a program to check if entered year is a leap year or not.

def leapYear(n):
    if(n % 4 == 0):
        return 1
    else: 
        return -1


n = int(input('Enter number : '))
res = leapYear(n)
if(res == 1):
    print(f'{n} is a leap year')
elif(res == -1):
    print(f'{n} is not a leap year')