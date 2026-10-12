class Emp:
    def __init__(self):
        print('Employee')

class SalesManager(Emp):
    def __init__(self):
        super().__init__()
        print('SalesManager')

class AreaManager(SalesManager):
    def __init__(self):
        super().__init__()
        print('AreaManager')
        
a = AreaManager()