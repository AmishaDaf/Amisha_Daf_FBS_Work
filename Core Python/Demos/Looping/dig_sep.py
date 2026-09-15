# sum is used to print the sum of digits we give as input

num = int(input('Enter number: '))
#sum = 0
while(num > 0):
    d = num % 10
    num = num // 10
    #sum += d
    print(d)
#print(sum)