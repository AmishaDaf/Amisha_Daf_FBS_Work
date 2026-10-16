class BankAccount:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def getAcc_no(self):
        return self.acc_no
    def setAcc_no(self, newacc_no):
        self.acc_no = newacc_no

    def getName(self):
        return self.name
    def setName(self, newname):
        self.name = newname

    def getBalance(self):
        return self.balance
    def setBalance(self, newbalance):
        self.balance = newbalance

    def display(self):
        print(f"Account_no. = {self.acc_no}\tName = {self.name}\tBalance = {self.balance}")

e1 = BankAccount(1234567889102, 'Amisha', 200000)
e2 = BankAccount(1232343454552, 'Gauri', 150000)
print(e1.getName())
e1.display()
e2.display()
e2.setBalance(190000)
e2.display()