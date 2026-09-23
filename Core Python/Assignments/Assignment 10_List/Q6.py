# 6. Write a program to remove duplicates from the list.


def Duplicate(li):
    size = len(li)
    search = li[0]
    for ind in range(1, size):
        if(li[ind] == search):
            return ind, li[end]
        search += ind
    else:
        return -1


li = [10, 20, 30, 40, 20, 10, 60, 10, 70]
res = Duplicate(li)
if(res != -1):
    print(res)
else:
    print('No duplicate element found')
