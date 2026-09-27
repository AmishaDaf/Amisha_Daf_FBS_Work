str = input("Enter a string: ")

rev = ""

for i in range(len(str) - 1, -1, -1):
    rev = rev + str[i]

print("Reverse string: ", rev)