#1. pass : Neglect expected indentation error
# for i in range(1, 10):
#     pass

#2. break : for terminating the loop

# for i in range(1, 10):
#     if(i == 4):
#         break
#     print(i)

#3. continue : To stop particilar iteration
# for i in range(1, 10):
#     if(i == 4):
#         continue
#     print(i)

#4. else : will execute when loop executed successfully
# for i in range(1, 10):
#     if(i==4):
#         break
#     print(i)
# else:
#     print('Else block executed')


for i in range(1, 10):
    if(i==4):
        continue
    print(i)
else:
    print('Else block executed')