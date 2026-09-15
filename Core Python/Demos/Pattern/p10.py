for i in range(1, 6):
    for j in range(1, 7-i):
        if(i+j==6 or i==1 or j==1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

