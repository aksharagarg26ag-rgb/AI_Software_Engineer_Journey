#Greeting function with default name.
def greet(name):
    print ("hello", name)

greet("Akshara")

#calculator:
def calculator(a,b,operation):
    if (operation == "add"):
        return a+b
    elif (operation == "subtract"):
        return a-b
    elif (operation == "mul"):
        return a*b
    elif (operation == "divide"):
        return a/b
print(calculator(3,4,"add"))

