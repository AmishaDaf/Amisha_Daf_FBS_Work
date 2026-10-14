class Employee:
    def __init__(self):
        print('Constructor',id(self))
    def display(self):
        print('Display of emp')
e1=Employee()
e2 = Employee()
print(f'id e1={id(e1)}')
print(f'id e1={id(e2)}')    
