#Bank account
class BankAccount:
    def __init__(self,balance):
        self.__balance= balance

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -=amount
        else:
            print("Insufficient balance")

    def show(self):
        print(self.__balance)

a1= BankAccount(1000)
a1.deposit(2000)
a1.withdraw(300)
a1.show()

#student class
class Student:
    def __init__(self,marks):
        self.__marks= marks

    def set_marks(self,marks):
        if marks >=0 and marks <=100:
            self.__marks= marks
        else:
            print("Invalid marks")
        
    def get_marks(self):
        return self.__marks
    
a1=Student(85)
print(a1.get_marks())

#Online Shopping Cart
class OnlineShopping:
    def __init__(self,price):
        self.__price=price

    def add_item(self,price):
        self.__price +=price

    def remove_item(self,price):
        if price <= self.__price:
            self.__price -= price
        else:
            print("No items to remove")

    def show_total(self):
        print(self.__price)

a1=OnlineShopping(500)
a1.add_item(400)
a1.remove_item(600)
a1.show_total()
