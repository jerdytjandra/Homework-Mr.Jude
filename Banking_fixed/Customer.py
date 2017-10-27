class Customer(object):
    def __init__(self, first_name, last_name, account_name):
        self.first_name = first_name
        self.last_name = last_name
        self.account_name = account_name

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_account(self):
        return self.account_name

    def set_account(self):
        first_name = input("INPUT YOUR FIRST NAME:")
        last_name = input("INPUT YOUR LAST NAME:")
        account_name = first_name + last_name
        print("ACCOUNT NAME: " + account_name)



