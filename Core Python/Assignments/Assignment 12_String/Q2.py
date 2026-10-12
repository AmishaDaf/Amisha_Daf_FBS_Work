# 2. Python Program to Remove the nth Index Character from a Non-Empty String

n = int(input('Enter number: '))
new_string = []
str ='FirstBit Solution'
new_string = str[:n] + str[n+1:]
print(new_string)