# 2. WAP to print all odd numbers until n.

# n = int(input('Enter number : '))
# i = 1
# while(i <= n):
#     if(i % 2 == 0):
#         pass
#     else:
#         print(i,end = ' ')
#     i+=1


n = int(input('Enter number : '))
for i in range(1, n):
    if(i % 2 != 0):
        print(i, end=' ')


