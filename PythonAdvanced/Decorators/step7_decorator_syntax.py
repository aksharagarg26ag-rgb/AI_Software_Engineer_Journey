def decorator(func):

    def wrapper():

        print("Function Started")

        func()

        print("Function Ended")

    return wrapper


@decorator
def greet():

    print("Hello Akshara")


greet()

#
def decorator(func):

    def wrapper():

        print("Start")

        func()

        print("End")

    return wrapper


@decorator
def study():

    print("Study")


@decorator
def sleep():

    print("Sleep")


study()

sleep()