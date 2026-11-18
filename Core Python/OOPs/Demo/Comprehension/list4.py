# li = [1, 3, 2, 5, 8, 16]
# l2 = []
# for i in li:
#     if(i % 2 == 0):
#         l2.append("even")
#     else:
#         l2.append("odd")
# print(l2)


li = [1, 3, 2, 5, 8, 16]
l2 = ["even" if i % 2 ==0 else "odd" for i in li ]
print(l2)