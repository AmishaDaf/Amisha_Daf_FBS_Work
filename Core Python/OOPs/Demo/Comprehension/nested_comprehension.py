# marks = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in range(len(marks)):
#     total = sum(marks[i])
#     print("Stu",i+1, "Total marks: ",  total)



# Not nested list
# li = []
# for i in range(1, 4):
#     for j in range(1, 4):
#         li.append(i*j)
# print(li)                           # [1, 2, 3, 2, 4, 6, 3, 6, 9]

# Traditional way
# li = []
# for i in range(1, 4):
#     row = []
#     for j in range(1, 4):
#         row.append(i*j)
#     li.append(row)
# print(li)                   # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

        

# Pythonic way
li = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(li)                   # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

