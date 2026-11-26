# def demo2():
#     print('I an in demo 2')
#     print(f'Name = {__name__}')             # Name = __main__
# def main():
#     demo2()
# main()

import demo1
def demo2():
    print('I an in demo 2')
    print(f'Name = {__name__}')             # Name = __main__

def greet():
    print('Welcome to FBS')
if __name__=="__main__":
    demo2()
    greet()
    demo1.demo1()
