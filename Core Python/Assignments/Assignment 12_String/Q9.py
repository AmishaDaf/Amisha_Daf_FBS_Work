# 9. Python Program to Calculate the Number of Words and the Number of Characters Present in a String 

# str = input('Enter string: ')
# count = 0
# w = 1
# for i in range(0, len(str)):
#     if(str[i] != ' '):
#         count += 1

#     if(str[i] == ' '):
#         w += 1

# print('Total length of string',len(str))
# print('No. of character is ',count)
# print('No. of word is ',w)


s = input("Enter a string: ")

words = s.split()
word_count = len(words)

chr_count = len(s.replace(" ", "")) 

char_count = len(s)

print("Number of words:", word_count)
print("Number of characters:", char_count)
print("Number of characters(without spaces):", chr_count)