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

class SavingAccount(BankAccount):
    def __init__(self, acc_no, name, balance, interest_rate):
        super().__init__(acc_no, name, balance)
        self.interest_rate = interest_rate
    def getInterest_rate(self):
        return self.interest_rate
    def setInterest_rate(self, ninterest_rate):
        self.interest_rate = ninterest_rate
    def display(self):
        print(f'Interest_rate = {self.interest_rate}\t')
        return super().display()

class CurrentAccount(BankAccount):
    def __init__(self, acc_no, name, balance, overdraft_limit):
        super().__init__(acc_no, name, balance)
        self.overdraft_limit = overdraft_limit
    def getOverdraft_limit(self):
        return self.Overdraft_limit
    def setInterest_rate(self, noverdraft_limit):
        self.overdraft_limit = noverdraft_limit
    def display(self):
        print(f'Overdraft_limit = {self.overdraft_limit}\t')
        return super().display()

b1 = BankAccount(1234567889102, 'Amisha', 200000)
s1 = SavingAccount(1232343454552, 'Gauri', 150000, 2)
c1 = CurrentAccount(1232343454552, 'Vedika', 150000, 1000)
b1.display()
s1.display()
c1.display()