# li = [3, 9, 10, 22, 11, 7, 2, 5]
# l2 = []
# for i in li:
#     if(i % 2 != 0):
#         l2.append(i**2)
# print(l2)


li = [3, 9, 10, 22, 11, 7, 2, 5]
l2 = [i**2 for i in li if i % 2 != 0]
print(l2)