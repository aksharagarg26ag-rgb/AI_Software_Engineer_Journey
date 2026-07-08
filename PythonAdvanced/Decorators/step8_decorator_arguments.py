def decorator(func):

    def wrapper(*args):

        print("Started")

        func(*args)

        print("Finished")

    return wrapper
@decorator
def greet(name):

    print(f"Hello {name}")

greet("Akshara")

@decorator
def student(name,age,course):

    print(name)
    print(age)
    print(course)

student("Akshara",20,"CSE")


#
import time

def timer(func):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print("Execution Time:", end-start)

        return result

    return wrapper


@timer
def calculate():

    total = 0

    for i in range(1000000):

        total += i

calculate()