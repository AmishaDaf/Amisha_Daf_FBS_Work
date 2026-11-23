# 1. Direct import
import demo1
demo1.add(12, 4)              # Addition = 16
print(demo1.a)              # 12
print(demo1.sub(12, 3))              # Subrtaction = 9          # None



# 2. From module name import member
from demo1 import sub
from demo1 import add
from demo1 import a
sub(12, 9)              # Subrtaction = 3
add(12, 3)              # Addition = 15
print(a)              # 12



# 3. From module name import Members
from demo1 import sub, add, a
print(a)              # 12
add(12, 3)              # Addition = 15



# 4. From modulename import All
from demo1 import *
sub(12, 7)              # Subrtaction = 5



# 5. Alice name
import demo1 as d
print(d.a)              # 12