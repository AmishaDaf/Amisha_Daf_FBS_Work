# 5. Accept a number from user and check if this element is present in the list or 
# not. Also tell how many times it is present in the list.


li = [10, 20, 30, 40, 20, 50, 20, 10]
n = int(input('Enter Element to search: '))
size = len(li)
count = 0
for ind in range(0, size):
    if(li[ind] == n):
        count += 1
        print('Element found at index: ',ind)

print('Element occurance count: ',count)
if count == 0:
    print("Element not found")
