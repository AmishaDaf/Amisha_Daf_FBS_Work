# 6. Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers. 
# Use the Python set.

s = list(map(int, input("Enter list elements: ").split()))
s1 = set()
max_product = 0
num1 = 0
num2 = 0
for i in s:
    for j in s1:
        product = i * j
        if max_product < product:
            max_product = product
            num1 = i
            num2 = j
    s1.add(i)
print("Numbers:", num1, "and", num2)
print("Maximum product:", max_product)