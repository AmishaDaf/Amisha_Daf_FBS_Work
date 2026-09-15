# 4. WAP to print Armstrong number within a given range

n = int(input('Enter range for armstrong number: '))

for i in range(1, n+1):
    temp = i
    count = 0
    while(temp > 0):
        count += 1
        d = temp % 10
        temp = temp // 10
     

    temp = i
    sum = 0
    while(temp > 0):
        d = temp % 10
        temp = temp // 10
        sum = sum + (d ** count)

    if(sum == i):
        print(i, end = ' ')

    