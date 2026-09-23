# 11. Write a program to accept an integer amount from user and tell minimum 
#     number of notes needed for representing that amount.

n = int(input('Enter amount: '))

n2000 = n // 2000
n = n % 2000

n500 = n // 500
n = n % 500

n200 = n // 200
n = n % 200

n100 = n // 100
n = n % 100

n50 = n // 50
n = n % 50

n20 = n // 20
n = n % 20

n10 = n // 10
n = n % 10

n5 = n // 5
n = n % 5

n2 = n // 2
n = n % 2

n1 = n // 1

tot_notes = n2000 + n500 + n200 + n100 + n50 + n20 + n10 + n5 + n2 + n1



print('Minimum number of notes requires is : ', tot_notes)