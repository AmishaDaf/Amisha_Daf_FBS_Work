var = 1
for i in range(1, 6):
    for j in range(1, 6-i):
        print('_', end=' ')

    for j in range(1, i+1):
        print(var, end=' ')
        var+=1
    print()