# 4. Python Program to Form a New String where the First Character and the Last Character have been Exchanged

str = (input('Enter string: '))
new = str[-1] + str[1:-1] + str[0]
print(str)
print(new)