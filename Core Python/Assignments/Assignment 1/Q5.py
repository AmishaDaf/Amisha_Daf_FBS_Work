# 5. Write a program to enter P, T, R and calculate Compound Interest.

P = int(input('Enter Amount: '))
R = int(input('Enter Rate: '))
T = int(input('Enter Time: '))

CI = P*(1+R/100)**T - P

print(f'Compound Interest is {CI}')