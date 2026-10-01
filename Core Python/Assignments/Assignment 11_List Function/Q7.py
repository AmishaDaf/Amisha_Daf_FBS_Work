# 7. Python Program to Find the Intersection of Two Lists 
l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]
l3 = []
for ind in range(0, len(l1)):
    for i in range(0, ind):
        if(l1[ind] == l2[i]):
            l3 += [l1[ind]]
print("List 1: ",l1)
print("List 2: ",l2)
print('Intersection: ',l3)
