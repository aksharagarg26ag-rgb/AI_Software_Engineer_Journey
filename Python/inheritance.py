#animal-dog
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d1= Dog()
d1.sound()


# use super() to call parent class method
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")

d1= Dog()
d1.sound()


#person - student
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Student(Person):
    def __init__(self,name,age,course,marks):
        super().__init__(name,age)
        self.course= course
        self.marks= marks

s1= Student("Akshara", 22, "B.Tech", 85)
print(s1.name,s1.course)

#vehicle car
class Vehicle:
    def __init__(self,brand,model):
        self.brand= brand
        self.model= model

class Car(Vehicle):
    def __init__(self,brand,model,price):
        super().__init__(brand,model)
        self.price= price

c1= Car("Toyota", "Camry", 25000)
print(c1.brand,c1.model,c1.price)