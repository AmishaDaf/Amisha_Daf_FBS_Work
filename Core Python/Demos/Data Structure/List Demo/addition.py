li = [10, 20, 30, 40, 50, 60, 70]
print(li)

# Method 1 : Iterating values
# sum = 0
# for ele in li:
#     # print(ele)
#     sum += ele
# print(sum)

# Method 2 : Using Indexing
sum = 0

for ind in range(0, len(li)):
    # print(ind)
    # print(li[ind])
    sum += li[ind]

print(sum)