def outer():

    message = "Hello Akshara"

    def inner():

        print(message)

    return inner


x = outer()

x()

#
def counter():

    count = 0

    def increment():

        nonlocal count

        count += 1

        print(count)

    return increment


c = counter()

c()
c()
c()

#
def login(user):

    def dashboard():

        print(user, "logged in")

    return dashboard


admin = login("Akshara")

admin()

#
def marks(score):

    def result():

        print("Marks:", score)

    return result


student_1= marks(95)
student_2= marks(88)
student_1()
student_2()