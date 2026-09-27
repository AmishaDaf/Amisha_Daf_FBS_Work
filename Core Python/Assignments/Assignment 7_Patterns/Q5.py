#         1
#       1   2
#     1       3
#   1           4
# 1   2   3   4   5

# for i in range(1, 6):
#     for j in range(1, 6-i):
#         print('-', end=' ')
#     print('1', end=' ')
#     for j in range(2, i+1):
#         if(i == 5):
#             print(f' {j}', end=' ')
#         else:
#             print('_',end=' ')
#     print()
    

rows = 5

for i in range(1, rows + 1):
    # 1. Print leading spaces for the outer pyramid structure
    print("  " * (rows - i), end="")
    
    # 2. Handle the top and middle rows (Rows 1 to 4)
    if i < rows:
        if i == 1:
            print("1")
        else:
            # Calculate internal spacing for the hollow center
            inner_spaces = " " * (4 * (i - 2) + 3)
            print(f"1{inner_spaces}{i}")
            
    # 3. Handle the bottom row (Row 5)
    else:
        # Loop through numbers 1 to 5 for the bottom line
        for j in range(1, rows + 1):
            if j == rows:
                print(j)  # Ends the line on the last number
            else:
                print(j, end="   ")
