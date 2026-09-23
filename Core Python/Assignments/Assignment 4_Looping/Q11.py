# 11. WAP to check if given number Strong Number.

n = int(input('Enter number: '))
temp = n
sum = 0
while(temp > 0):
    d = temp % 10
    temp = temp // 10
    print(d)
    fact = 1
    for i in range(1, d+1):
        fact = fact * i
    sum = sum + fact

if(n == sum):
    print(f'{n} is strong number')
else:
    print(f'{n} is not strong number')