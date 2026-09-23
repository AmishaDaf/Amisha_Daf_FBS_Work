# 11. WAP to check if a given number is Armstrong number or not. For
# each task create separate functions.



def Armstrong(n):
    temp = n
    count = 0
    while(temp > 0):
        temp = temp // 10
        count += 1
    return count


def Arm(n, count):
    temp = n
    sum = 0
    while(temp > 0):
        d = temp % 10
        temp = temp // 10
        sum = sum + (d ** count)
    return sum


n = int(input('Enter number: '))
res = Armstrong(n)
result = Arm(n, res)
if(result == n):
    print(f'{n} is an Armstrong number')
else:
    print(f'{n} is not an Armstrong number')





