class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")

d1= Dog()
c1= Cat()   
d1.sound()  # Output: Dog barks
c1.sound()  # Output: Cat meows 

#calculator:
class Calculator:
    def __add__(self,a=0,b=0,c=0):
        return a+b+c
    
print(Calculator().__add__(2,5,6))

#payment system
class Payment:
    def pay(self,amount):
        print("payment successful")
class UPI(Payment):
    def pay(self,amount):
        print("payment successful through UPI")
class CreditCard(Payment):
    def pay(self,amount):
        print("payment successful through Credit Card")
class PayPal(Payment):
    def pay(self,amount):
        print("payment successful through PayPal")
payment_methods= [UPI(), CreditCard(), PayPal()]
for method in payment_methods:
    method.pay(100)
print(Payment().pay(300))