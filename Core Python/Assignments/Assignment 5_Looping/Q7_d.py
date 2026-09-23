# 7. Write a program to solve the following series :
# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
 
n = int(input('Enter number: '))
sum = 0
for i in range(1, 11):
    sum = sum + ((n**i)/i)
print(sum)
   


