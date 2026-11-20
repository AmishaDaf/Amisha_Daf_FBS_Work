# def demo1():
#     print("I am in demo")
# a = 10
# print(type(a))              # <class 'int'>
# print(type(demo1))          # <class 'function'>


#______ 1. Understand that Function is the Object of Function Class
# def demo1():
#     print("I am in demo")       # <class 'function'>
# print(type(demo1))



#______ 2. We can store the function in variable
# def demo1():
#     print("I am in demo")
# print(type(demo1))       # <class 'function'>
# x = demo1
# x()                         # I am in demo





# def hi():
#     print("I am in Hi")
# def demo(a):
#     print(a)                    # <function hi at 0x000002D2955DFAB0>
# demo(hi)



#______ 3. We can pass Function Parameter to another function
# def hi():
#     print("I am in Hi")
# def demo(a):                                 
#     print("I am in demo")                    # I am in demo
#     a()                                      #  I am in Hi 
# demo(hi)



#______ 4. We can return a Function from inside the function
# def outerFun():
#     print('outerfun')
#     def innerFun():
#         print('innerFun')       # outerfun
#     return innerFun
# res = outerFun()
# # print(res)                  # <function outerFun.<locals>.innerFun at 0x0000015BBE2E35E0>
# res()                  # innerFun


# def outerFun():
#     print('outerfun')
#     a = 33
#     def innerFun():
#         print('innerFun')       # outerfun
#     a = innerFun
#     return a
# res = outerFun()
# # print(res)                  # <function outerFun.<locals>.innerFun at 0x0000015BBE2E35E0>
# res()                  # innerFun



#______ 5. Closure - Special type of function which pass everything to its neighbour function.
# def demo(a = 10):
#     def innerFun():
#         print(a)
#     return innerFun
# res = demo()
# # print(res)              # <function demo.<locals>.innerFun at 0x00000179A19D35E0>
# res()                       # 10




# def decore(x):
#     print('I am in decorator')  # I am in decorator
#     def innerFun():             # Logger Added
#         print('Logger Added')   # Time started
#         print('Time started')   # I am in log in
#         x()                     # Time stopped
#         print('Time stopped')   # Logger Removed
#         print('Logger Removed')
#     return innerFun
# def login():
#     print('I am in log in')
# res = decore(login)
# res()





# def decore(x):
#     print('I am in decorator')  # I am in decorator 3
#     def innerFun():             # Logger Added 2 2
#         print('Logger Added')   # Time started 2 2
#         print('Time started')   # I am in log in 1
#         x()                     # Time stopped 2 2
#         print('Time stopped')   # Logger Removed 2 2
#         print('Logger Removed')
#     return innerFun

# @decore
# def login():
#     print('I am in log in')

# @decore
# def logout():
#     print('I am in log out')   
# res = decore(login)
# res()
# res1 = decore(logout)
# res1()





# def decore(x):
#     print('\nI am in decorator')  # I am in decorator 3
#     def innerFun(*a):             # Logger Added 2 2
#         print('Logger Added')   # Time started 2 2
#         print('Time started')   # I am in log in 1
#         x(*a)                     # Time stopped 2 2
#         print('Time stopped')   # Logger Removed 2 2
#         print('Logger Removed')
#     return innerFun

# @decore
# def login():
#     print('I am in log in')

# @decore
# def logout():
#     print('I am in log out')   

# @decore
# def add(a, b):
#     print(f'Addition = {a+b}')

# res = decore(login)
# res()
# res1 = decore(logout)
# res1()
# login()
# logout()
# add(1, 2)