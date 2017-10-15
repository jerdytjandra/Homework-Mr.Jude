from BANKING.Account import Account
from BANKING.Bank import Bank
from BANKING.Customer import Customer


def main():
    num = input("INPUT NUMBER OF CUSTOMER:")
    custs = input("INPUT NAME OF CUSTOMER:")
    contoh = Bank(custs, num, "BANK JERDY")
    contoh.bank_info()
    print("\n####WELCOME TO ATM JERDY#####")
    menu_1 = input("(PLEASE INPUT A NUMBER.)"
                   "\nWOULD YOU LIKE TO:"
                   "\n[1]LOG IN"
                   "\n[2]SET A NEW ACCOUNT\n")
    if   menu_1 == "1":
        user = input("INPUT USERNAME:")
        password = input("INPUT PASSWORD:")
        #PASSWORD = *********(9*)
        user = Account(10000000)
        user.account_info()
        while True:
            menu_user = int(input("WHAT WOULD YOU LIKE TO DO?"   
                                "\n[1]DEPOSIT"                
                                "\n[2]WITHDRAW"               
                                "\n[3]EXIT\n"))
            if menu_user == 1:
                user.deposit(int(input("INPUT AMMOUNT:")))
                user.account_info()
            elif menu_user == 2:
                user.withdraw(int(input("INPUT AMOUNT:")))
                user.account_info()
            elif menu_user == 3:
                exit()

    elif menu_1 == "2":
        while True:
            set_acc = input("(PLEASE INPUT A NUMBER.)"
                            "\nWOULD YOU LIKE TO SET A NEW ACCOUNT?"
                            "\n[1]YES"
                            "\n[2]NO\n")
            if set_acc == "1":
                customer = Customer("", "", "")
                customer.set_account()
            elif set_acc == "2":
                exit()
            customer = Account(0000000)
            customer.account_info()
            while True:
                menu_2 = int(input("WHAT WOULD YOU LIKE TO DO?"
                                    "\n[1]DEPOSIT"
                                    "\n[2]WITHDRAW"
                                    "\n[3]EXIT\n"))
                if menu_2 == 1:
                    customer.deposit(int(input("INPUT AMMOUNT:")))
                    customer.account_info()
                elif menu_2 == 2:
                    customer.withdraw(int(input("INPUT AMOUNT:")))
                    customer.account_info()
                elif menu_2 == 3:
                    exit()
main()
