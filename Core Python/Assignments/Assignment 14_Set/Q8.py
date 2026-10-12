# 8. Write a Python program to find all the anagrams and group them together from a given list of strings.

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
d = {}
for word in words:
    sorted_word = ''.join(sorted(word))
    if sorted_word not in d:
        d[sorted_word] = []
    d[sorted_word].append(word)
print(d)
