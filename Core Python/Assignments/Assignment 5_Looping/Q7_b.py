# 7. Write a program to solve the following series :
# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)

n = int(input('Enter number: '))
ex = 0
for i in range(1, n+1):
    ex = ex + n ** i
print('Sum of series is : ', ex)