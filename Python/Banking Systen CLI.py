#Banking system
class Bank:

    def __init__(self, account_name, account_number, money):
        self.account_name= account_name
        self.account_number=account_number
        self.money= money

    def display(self):
        print("Your Account details are : ")
        print("Account Name: ", self.account_name)
        print("Account Number: ", self.account_number)
        print("Amount currently in Bank: ", self.money)

Bank_list = []

while True:
    print("Banking System!")
    print("Features")
    print("1. create account")
    print("2. deposit")
    print("3. withdraw")
    print("4. check balance")

    choice = input("Enter your choice to do: ")
    
    if not choice.isdigit():
        print("Please enter number")
        continue
    else:
        choice = int(choice)

    if(choice == 1):
        print("Lets proceed with Account Creation")
        acc_name= input("Enter account name: ")

        try:
            acc_number= int(input("Enter account number: "))
            acc_amount= int(input("Enter account amount: "))

            details= Bank(acc_name, acc_number, acc_amount)
            Bank_list.append(details)
            print("Account added!")
            for details in Bank_list:
                details.display()

        except ValueError:
            print("Enter valid account number")

    elif(choice ==2):
        check_account=  int(input("Enter account number to deposit money: "))
        found =False
        for account in Bank_list:
            if account.account_number == check_account:
                deposit_value= int(input("Enter amount to deposit: "))
                account.money += deposit_value
                print("Money deposited successfully")
                for details in Bank_list:
                    details.display()

                found = True

        if not found:       
            print("Account not found")

    elif(choice==3):
        check_account=int(input("Enter account number to withdraw money: "))
        found = False
        for account in Bank_list:
            if account.account_number ==check_account:
                withdraw_amount=  int(input("Enter amount to withdraw: "))
                account.money -= withdraw_amount
                print("Money is Withdraw")
                for details in Bank_list:
                    details.display()

                found= True

        if not found:
            print("Account not found")

    elif(choice==4):
        if len(Bank_list) == 0:
            print("No accounts found")

        else:
            for details in Bank_list:
                details.display()


    else:
        print("Invalid ")
     

