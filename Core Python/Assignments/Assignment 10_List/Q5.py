# 5. Accept a number from user and check if this element is present in the list or 
# not. Also tell how many times it is present in the list.



def Search(li, search_ele):
    size = len(li)
    for ind in range(0, size):
        if(li[ind] == search_ele):
            return ind
    else:
        return -1

li = [10, 20, 30, 40, 50, 60, 70]
n = int(input('Enter element to search: '))
res = Search(li, n)
if(res != -1):
    print(f'Element present at index {res}')
else:
    print('Element not found')
