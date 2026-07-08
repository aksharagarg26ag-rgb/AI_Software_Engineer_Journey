def outer():

    def inner():

        print("Hello from Inner Function")

    return inner


x = outer()

print(x)

#
def outer():

    def inner():

        print("Hello from Inner Function")

    return inner


x = outer()

x()

#
def outer():

    def inner():

        print("Hello")

    return inner


outer()()

#
def add():

    print("Addition")


def multiply():

    print("Multiplication")


def calculator(choice):

    if choice == 1:

        return add

    else:

        return multiply


operation = calculator(1)

operation()

#
def study():

    print("Studying")
def sleep():

    print("Sleeping")
def action(choice):

    if choice == 1:

        return study

    else:

        return sleep
action(1)()