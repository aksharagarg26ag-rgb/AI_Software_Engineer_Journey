def outer():

    print("Outer Function")

    def inner():

        print("Inner Function")

    inner()

outer()

#
def outer():

    print("Welcome")

    def study():

        print("Studying Python")

    def sleep():

        print("Sleeping")

    study()

outer()


#
def outer():

    print("Daily Routine")

    def study():

        print("Studying")

    def sleep():

        print("Sleeping")

    study()

    sleep()

outer()

#
def company():
    print("Company started")
    def manager():
        print("Manager is working")
        def employee():
            print("Employee is working")
        employee()
    manager()   
company()