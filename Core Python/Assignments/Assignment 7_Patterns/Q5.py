for i in range(1, 6):
    # for i in range(1, 6-i):
    #     print('_',end =' ')


    for j in range(1, i+1):
        if(i==j or i == 5 or j==1):
            print(j, end=' ')
        else:
            print(' ', end=' ')

    print()