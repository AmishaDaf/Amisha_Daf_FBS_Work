# 12. Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
# 4*4*4*4)

n = int(input('Enter number: '))
temp = n
count = 0

while(temp > 0):
    count += 1
    d = temp % 10
    temp = temp // 10 
    print(d)

temp = n
sum = 0
while(temp > 0):
    d = temp % 10
    temp = temp // 10
    sum = sum + (d ** count)

if(n == sum):
    print(f'{n} is an Armstrong number')
else:
    print(f'{n} is not Armstrong number')



