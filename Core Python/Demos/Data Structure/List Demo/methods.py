li = [40, 10, 30, 20, 10]

li.append(50)
print(li)

li.clear()
print(li)

li2 = li.copy()
print(li)

li3 = li
print(li)

li.append(50)
print(li)

print(li2)
print(li3)

print(li.count(10))
print(li)

li.extend([60, 70, 80])
print(li)

print(li.index(50))
print(li)

li.insert(2, 70)
print(li)

li.pop()
print(li)

li.pop(2)
print(li)

li.pop(10)      ### IndexError: pop index out of range
print(li)

li.remove(50)   ### ValueError: list.remove(x): x not in list
print(li)

li.reverse()
print(li)

li.sort()
print(li)

li.sort(reverse = True)
print(li)