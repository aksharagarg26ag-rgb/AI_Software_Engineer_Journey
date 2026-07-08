def logger(func):

    def wrapper(*args, **kwargs):

        print("Logger Started")

        result = func(*args, **kwargs)

        print("Logger Finished")

        return result

    return wrapper

import time

def timer(func):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(f"Execution Time: {end-start:.5f} seconds")

        return result

    return wrapper

@logger
@timer
def study():

    print("Studying Python")

study()


#
logged_in = True

def authentication(func):

    def wrapper(*args, **kwargs):

        if logged_in:

            print("Authentication Success")

            return func(*args, **kwargs)

        else:

            print("Access Denied")

    return wrapper
@authentication
@logger
@timer
def dashboard():

    print("Dashboard Opened")

dashboard()