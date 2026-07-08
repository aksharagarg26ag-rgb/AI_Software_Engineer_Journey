def greet():
    print("Hello, Welcome to Python!")

print(greet)


def greet():
    print("Hello, Welcome to Python!")

print(greet())

def greet():
    print("Hello!")
say_hello = greet
say_hello()


def greet():
    print("Hello")
x = greet
greet()
x()

def greet():
    print("Hello")
x = greet
print(type(x))


def add():
    print("Add")
def delete():
    print("Delete")
operations = [add, delete]
operations[0]()
operations[1]()


def add():
    print("Adding")
def delete():
    print("Deleting")
menu = {
    "1": add,
    "2": delete
}
menu["1"]()
menu["2"]()


def study():
    print("Studying")
def sleep():
    print("Sleeping")
def eat():
    print("Eating")
action=[study, sleep, eat]
for a in action:
    a()
