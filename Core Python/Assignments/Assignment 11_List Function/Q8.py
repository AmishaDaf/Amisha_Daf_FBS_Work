# 8. Print 1 to 100 in snakes and ladder pattern.

# l1 = []
# l2 = []
var = 1
for row in range(1, 11):
    l1 = []
    for col in range(1, 11):
        # if(row % 2 != 0):
        l1 += (list([var]))
        var += 1
    if(row % 2 != 0):
        print(l1)
    if(row % 2 == 0):
        l1.reverse()
        print(l1)




