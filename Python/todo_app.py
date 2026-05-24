task=[]
while True:
    print("Features:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")

    user= input("Enter your choice")

    if user.isdigit():
        user = int(user)
    else:
        print("invalid input")
        continue
 
    if user==1 :
        add_task= str(input("Enter task"))
        task.append(add_task)
        print("Task added successfully!")
    elif user == 2: 
        remove_task= str(input("Enter task to remove"))
        if remove_task in task: 
            task.remove(remove_task)
            print("Task removed successfully!")

        else: print("Task not found")
    elif user==3:
        print(task)
    else:
        print("Invalid choice")   