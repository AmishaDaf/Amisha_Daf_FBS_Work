# 7. Write a program to solve the following series :
# e. x - x2/3 + x3/5 - x4/7 + .... to n terms

r = int(input('Enter range: '))
n = int(input('Enter number: '))
sum = 0
for i in range(1, r+1):
    term = (n**i)/(2*i-1)
    # a += 2

    if(i % 2 == 0):
        sum = sum - term
    else:
        sum = sum + term
print(sum)