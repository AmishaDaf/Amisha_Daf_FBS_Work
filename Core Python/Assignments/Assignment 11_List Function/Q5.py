# 5. Python Program to Sort a List According to the Length of the Elements within the list.

li = ["apple", "cat", "banana", "hi", "dog"]

li.sort(key=lambda x: len(x))

print(li)