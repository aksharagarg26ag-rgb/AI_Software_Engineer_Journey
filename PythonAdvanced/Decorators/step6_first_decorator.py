def greet():

    print("Hello Akshara")


print("Function Started")

greet()

print("Function Ended")

#
def decorator(func):

    def wrapper():

        print("Function Started")

        func()

        print("Function Ended")

    return wrapper


def greet():

    print("Hello Akshara")


greet = decorator(greet)

greet()