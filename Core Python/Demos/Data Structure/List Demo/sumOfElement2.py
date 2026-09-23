li = [5, [10, 20], [30, 40], [50, 60]]

sum = 0
for i in range(len(li)):
    if(type(li) == list):
        for j in range(len(li[i])):
            sum += li[i][j]
    else: 
        sum += li[i]
print(sum)