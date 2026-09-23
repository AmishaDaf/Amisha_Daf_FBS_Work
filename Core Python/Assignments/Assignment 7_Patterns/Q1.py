#         * 
#       *   * 
#     *       * 
#   *           * 
# *               * 
# *               * 
#   *           * 
#     *       * 
#       *   * 
#         * 



# for i in range(1, 6):
#     for j in range(1, 7-i):
#         if((i+j) == 6):
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')

#     for j in range(1, i):
#         print(' ', end=' ')
    
#     print()


for i in range(1, 6):

    # spaces before first *
    for j in range(1, 6 - i):
        print(' ', end=' ')

    # first *
    print('*', end=' ')

    # spaces between stars and second *
    if i > 1:
        for j in range(1, 2 * i - 2):
            print(' ', end=' ')

        print('*', end=' ')

    print()


for i in range(5, 0, -1):

    # spaces before first *
    for j in range(1, 6 - i):
        print(' ', end=' ')

    # first *
    print('*', end=' ')

    # spaces between stars and second *
    if i > 1:
        for j in range(1, 2 * i - 2):
            print(' ', end=' ')

        print('*', end=' ')

    print()