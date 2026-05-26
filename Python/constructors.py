#Bank Account
class Bank_account:
    def __init__(self,account_name, balance):
        self.account_name= account_name
        self.balance= balance   

    def deposit(self,amount):
        self.balance += amount
        print("Amount deposited")

    def withdraw(self,amount):
        self.balance -=amount
        print("Amount withdrawn")

    def show_balance(self):
        print(self.balance)


a1=Bank_account("akshara", 10000)
a1.deposit(5000)
a1.show_balance()
a1.withdraw(2000)
a1.show_balance()