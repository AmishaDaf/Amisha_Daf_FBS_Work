# 9. Write a program of having n number of elements in the list and find out even 
# and odd elements in that list and then create two separate lists which will have 
# even elements and other will have odd elements.


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 3, 5, 4, 5]
l2 = []
l3 = []
for ind in range(0, len(l1)):
    if(l1[ind] % 2 == 0):
        l2 += [l1[ind]]
    else:
        l3 += [l1[ind]]
print(l1)
print(l2)
print(l3)