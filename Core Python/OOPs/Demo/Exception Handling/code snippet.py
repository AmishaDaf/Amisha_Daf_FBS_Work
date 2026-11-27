# try:
#     print(10//0)            # ZeroDivisionError: division by zero
# finally:
#     print('Finally')

# print('Hello')



# try:
#     print('A')
#     raise Exception('I am in try block')        # A     # I am in try block
#     print('B')
# except Exception as e:
#     print(e)
# else:
#     print('I am in else')



# def add():
#     try:
#         return 'ABC'            # Finally
#                                 # ABC
#     finally:
#         print('Finally')
# print(add())




# try:
#     print('Start')
#     try:
#         print(10//0)              # Start             # H division by zero
#     except Exception as e:
#         print('H', e)
# except Exception as e:
#     print('Hello', e)




# try:
#     print(10//0)
#     try:
#         print(10//0)              # Outer Exception =  division by zero
#     except Exception as e:
#         print('Inner Exception = ', e)
# except Exception as e:
#     print('Outer Exception = ', e)



try:
    print(10//5)
except Exception as e:
    print(e)
else:
    print(10//0)            # ZeroDivisionError: division by zero
finally:
    print('Finally')