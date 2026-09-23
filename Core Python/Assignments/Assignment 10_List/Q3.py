# 3. Write a program to find the second largest element in the list. 

li = [20, 40, 10, 70, 50, 60, 30]
max = li[0]
smax = 0
for ind in range(1, len(li)):
    if(li[ind] > max):
        smax = max
        max = li[ind]
    elif(li[ind] > smax):
        smax = li[ind]
print(f'Second largest element in the list is: {smax}')
        
