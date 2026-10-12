# 5. Write a Python program to find the longest common prefix of all strings. Use the Python set.

words = ["flower", "flow", "flight"]
prefix = ""
shortest = min(words, key=len)
for i in range(len(shortest)):
    s = set()
    for word in words:
        s.add(word[i])
    if len(s) == 1:
        prefix += shortest[i]
    else:
        break
print("Longest common prefix:", prefix)