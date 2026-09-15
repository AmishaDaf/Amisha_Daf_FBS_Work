# 7. WAP to print all integers upto n that aren’t divisible by 2 and 3.

n = int(input('Enter number: '))
for i in range(2, n):
    if(i % 2 != 0 and i % 3 != 0):
        print(i)
    i+=1