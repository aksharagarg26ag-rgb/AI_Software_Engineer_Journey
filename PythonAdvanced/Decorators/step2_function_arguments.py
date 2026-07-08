def square(x):
    return x * x

print(square(5))

#
def greet():
    print("Hello!")

def execute(func):

    print("Inside execute()")

    func()

execute(greet)


#
def add():
    print("Adding...")

def delete():
    print("Deleting...")

def execute(task):

    print("Starting Task")

    task()

    print("Task Finished")

execute(add)

execute(delete)


#
def add():

    print(10 + 20)

def multiply():

    print(10 * 20)

def calculate(operation):

    operation()

calculate(add)

calculate(multiply)

#
def eat():
    print("Eating")

def study():
    print("Studying")

def sleep():
    print("Sleeping")

tasks = [eat, study, sleep]

for task in tasks:

    task()


#
def welcome(name):

    print(f"Welcome {name}")

def goodbye(name):

    print(f"Goodbye {name}")

def execute(func, name):
    print("Executing Function")
    func(name)
    print("Function Executed")
execute(welcome, "Akshara")
execute(goodbye, "Akshara")