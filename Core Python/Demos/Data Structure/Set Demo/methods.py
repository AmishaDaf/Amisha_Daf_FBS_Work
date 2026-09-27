s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}
s3 = {50, 60}
# s1.add(50)            # {40, 10, 50, 20, 30}
# s1.clear()            # set()
# s5 = s1.copy()        # {40, 10, 20, 30}
# print(s1.difference(s2))          # {10, 20}
# s1.difference_update(s2)          # {20, 10}
# s1.discard(50)                # {40, 10, 20, 30}
# print(s1.intersection(s2))            # {40, 30}
# s1.intersection_update(s2)            # {40, 30}
# print(s1.isdisjoint(s3))              # True
# print(s3.issubset(s2))                # True
# print(s2.issuperset(s3))              # True


#s4 = {50, 60}   ### s3 & s4 are subset & superset of each other

# s1.pop()                                      # {10, 20, 30}
# s1.remove(50)                                    # KeyError: 50      error
# print(s1.symmetric_difference(s2))                # {10, 50, 20, 60}
# s1.symmetric_difference_update(s2)                # {10, 50, 20, 60}
# print(s1.union(s2))                           # {40, 10, 50, 20, 60, 30}
# s1.update({70, 80, 90})                       # {80, 20, 90, 70, 40, 10, 30}



print(s1)