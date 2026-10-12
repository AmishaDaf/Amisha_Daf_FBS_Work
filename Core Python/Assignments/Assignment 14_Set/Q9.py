# 9. Write a Python program to find all the unique combinations of 3 numbers from a given list of numbers, adding up to a target number.

num = [2, 3, 4, 5, 6, 7]

target = int(input('Enter number: '))
for i in num:
    for j in num:
        for k in num:
            if(i<j<k):
                if (i + j + k == target):
                    first = i
                    second = j
                    third = k
                    print('Combination of target number is ',first, second, third)

