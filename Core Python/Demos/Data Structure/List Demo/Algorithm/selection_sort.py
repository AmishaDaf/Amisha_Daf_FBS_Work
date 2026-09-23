def selectionSort(li):
    size = len(li)
    for i in range(0, size-1):
        mid_ind = i
        for j in range(i+1, size):
            if(li[j] < li[mid_ind]):
                mid_ind = j
        li[i], li[mid_ind] = li[mid_ind], li[i]
        # print(li)

li = [50, 40, 30, 20, 10]
print(li)
selectionSort(li)
print(li)