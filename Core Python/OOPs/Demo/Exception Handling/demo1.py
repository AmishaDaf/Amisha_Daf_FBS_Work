try:
    a = int(input('Enter num 1: '))
    b = int(input('Enter num 2: '))
    print(a//b)
except ZeroDivisionError as z:
    print(f'Zero division {z}')
except ValueError as v:
    print(f'Value error {v}')
except Exception as e:
    print(f'Exception {e}')
else:
    print('I am in else block')
finally:
    print('I am in Finally block')

