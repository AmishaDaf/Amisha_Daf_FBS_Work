# t = (10, 20, 30)
# t = t + (40,)
# print(t)


t = (10, 20, 30)
li = list(t)
print(li)           # [10, 20, 30]
li.append(40)
print(li)           # [10, 20, 30, 40]
t = tuple(li)

print(t)            # (10, 20, 30, 40)