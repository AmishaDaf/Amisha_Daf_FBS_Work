# 5. Python Program to Count the Number of Vowels in a String

str = (input('Enter String: '))
count = 0
for i in range(0, len(str)):
    if(str[i] == 'a' or str[i] == 'e' or str[i] == 'i' or str[i] == 'o' or str[i] == 'u'):
        count += 1

print(f'There is {count} vowels in string')