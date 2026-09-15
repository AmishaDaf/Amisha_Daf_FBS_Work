# 1. WAP to print all even numbers until n.

n = int(input('Enter value of n: '))
i = 1
while(i <= n):
    if(i % 2 == 0):
        print(i,end = " ")
    i+=1
    
