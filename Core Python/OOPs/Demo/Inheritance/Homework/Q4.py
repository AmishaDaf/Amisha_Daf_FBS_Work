class Payment:
    def __init__(self, payment_id, amount, date):
        self.payment_id = payment_id
        self.amount = amount
        self.date = date

    def getPayment_id(self):
        return self.payment_id

    def setPayment_id(self, newpayment_id):
        self.payment_id = newpayment_id

    def getAmount(self):
        return self.amount

    def setAmount(self, newamount):
        self.amount = newamount

    def getDate(self):
        return self.date

    def setDate(self, newdate):
        self.date = newdate

    def display(self):
        print(f"Payment ID = {self.payment_id}\tAmount = {self.amount}\tDate = {self.date}")


class CashPayment(Payment):
    def __init__(self, payment_id, amount, date, received_by):
        super().__init__(payment_id, amount, date)
        self.received_by = received_by

    def getReceived_by(self):
        return self.received_by

    def setReceived_by(self, newreceived_by):
        self.received_by = newreceived_by

    def display(self):
        print(f"Received By = {self.received_by}\t")
        return super().display()


class CardPayment(Payment):
    def __init__(self, payment_id, amount, date, card_type):
        super().__init__(payment_id, amount, date)
        self.card_type = card_type

    def getCard_type(self):
        return self.card_type

    def setCard_type(self, newcard_type):
        self.card_type = newcard_type

    def display(self):
        print(f"Card Type = {self.card_type}\t")
        return super().display()


p1 = Payment(101, 5000, "07-10-2026")
c1 = CashPayment(102, 2500, "07-10-2026", "Amisha")
c2 = CardPayment(103, 7500, "07-10-2026", "Credit Card")
p1.display()
c1.display()
c2.display()