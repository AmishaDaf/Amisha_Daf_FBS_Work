# 8. Write a program find reverse of a number

def revNumber(n):
    temp = n
    rev = 0
    while(temp > 0):
        d = temp % 10
        temp = temp // 10
        rev = rev * 10 + d
    return rev


n = int(input('Enter number : '))
res = revNumber(n)
print(f'Reverse of {n} is {res}')