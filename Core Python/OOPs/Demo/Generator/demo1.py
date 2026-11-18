# def genNo():
#     a = 10
#     b = a
#     a +=1
#     return b
# print(genNo())      # 10




# def genNo():
#     return [i for i in range(1, 11)]
# print(genNo())          # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



# def genNo():
#     yield(10)
# d = genNo()
# print(d)            # <generator object genNo at 0x000001CE7A8D53C0>




# def genNo():
#     for i in range(1, 11):
#         yield(i)
# d = genNo()
# print(next(d))              # 1
# print(next(d))              # 2




# def genNo():
#     yield(20)
#     yield(30)
#     yield(40)
# d = genNo()
# print(next(d))              # 20
# print(next(d))              # 30
# print(next(d))              # 40





# def genNo():
#     yield(20)
#     yield(30)
#     yield(40)
# d = genNo()
# print(next(d))              # 20
# print(next(d))              # 30
# print(next(d))              # 40
# print(next(d))              # error - StopIteration




# def genNo():
#     yield(20)
#     print("Stop 1")
#     yield(30)
#     print("Stop 2")
#     yield(40)
#     print("Stop 3")
# d = genNo()
# print(next(d))          # 20
# print(next(d))          # 20    # Stop 1    # 30
# print(next(d))          # 20    # Stop 1    # 30    # Stop 2    # 40




def genNo():
    for i in range(1, 100, 10):
        yield(i)
d = genNo()
print(next(d))          # 1
print(next(d))          # 11
print(next(d))          # 21
print(next(d))          # 31
print(next(d))          # 41

