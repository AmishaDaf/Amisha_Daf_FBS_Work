# 6. Write a program to remove duplicates from the list.


li = [10, 20, 10, 30, 20, 40]

unique = []


for ind in range(0, len(li)):
    found = 0
    for j in range(len(unique)):
        if(li[ind] == unique[j]):
            found = 1
            break
    if (found == 0):
        unique = unique + [li[ind]]

print('Before duplication: ',li)
print('After duplication: ',unique)




