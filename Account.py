class Account(object):
    def __init__(self, balance):
        self.balance = balance

    def account(self, amt):
        self.account = amt

    def get_balance(self):
        return self.balance

    def deposit(self, amt):
        if amt > 0:
            self.balance = self.balance + amt

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance = self.balance - amt

    def account_info(self):
        print("ACCOUNT BALANCE:", self.balance)

