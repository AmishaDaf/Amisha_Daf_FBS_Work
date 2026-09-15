x = 10
y = 10
z = 20

li1 = [10, 20]
li2 = [10, 20]

#1. is   check memory address 
print(x is y)           #T
print(li1 is li2)       #F

print(id(x))    # use to show or check the adress, it is same for both x and y
print(id(y))
print(id(li1))
print(id(li2))

#2. is not
print(li1 is not li2)       #T
print(x is not y)           #F