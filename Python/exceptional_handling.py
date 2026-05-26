# try: 
#     num=int(input())
#     print(10/num)

# except:
#     print("invalid")


# try:
#     n= int(input())
#     print(10/n)

# except ZeroDivisionError:
#     print("invalid")

# except ValueError:
#     print("wrong")
    
# finally:
#     print("finish")

#expense trackr
while True:
    print("Features:")
    print("1. Add Expense")
    print("2.View expense")
    print("3. Exit")

    choice= input("Enter your choice")

    if not choice.isdigit():
        print("Please enter number")
        continue
    else: 
        choice = int(choice)

    if (choice==1):
        expense= input("Enter name:")

        try:
            amount = float(input("Enter expense amount"))
            with open("expense.txt", "a") as file:
                file.write(f"{expense} - {amount}\n")
                print("Expense added!")

        except ValueError:
            print("Invalid amount")

    elif (choice==2):
        with open("expense.txt", "r") as file:
            print(file.read())

    elif(choice== 3):
        file.close()

    
            



