# 4.  Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.

n = int(input('Enter number: '))
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s1 = set()
for i in s:
    required = n - i
    if required in s1:
        print(f'Pair found ({i} , {required})')
    else:                                               #if required not in s1
        s1.add(i)
    




