class Bank(object):
    def __init__(self, customers, num_customer,bank_name):
        self.customers = customers
        self.bank_name = bank_name
        self.num_customer = num_customer

    def get_num_customer(self):
        return self.num_customer

    def add_customers(self):
        num_customers = []
        num_customers.append(input("Input a name:"))
        print(num_customers)

    def bank_info(self):
        print("CUSTOMER(S):", self.customers, "\nBANK NAME:", self.bank_name, "\nNUMBER OF CUSTOMER(s):", self.num_customer)

    def get_customer(self):
        return self.customers


