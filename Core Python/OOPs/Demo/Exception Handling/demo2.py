try:
    n1 = int(input('Enter the number 1: '))
    n2 = int(input('Enter the number 2: '))
    if n2>0:
        print(n1//n2)
    else:
        raise Exception('You entered wrong inout in number 2')
except Exception as e:
    print(e)