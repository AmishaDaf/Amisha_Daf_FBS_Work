# 4. Write a program to enter P, T, R and calculate simple Interest.

P = int(input('Enter Amount: '))
R = int(input('Enter rate: '))
T = int(input('Enter time: '))

SI = (P*R*T)/100

print(f'Simple interest is {SI}')
