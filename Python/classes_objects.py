# class Student:
#     salary= 10000
#     def __init__(self,name,age,course):
#         self.name= name
#         self.age = age
#         self.course= course


#     #change salary
#     @classmethod
#     def change_salary(cls, newsalary):
#         cls.salary = newsalary

# #instance of the class
# akshara= Student("Akshara"," 22", "btech")
# print(akshara.name, akshara.age, akshara.course)

# Student.change_salary(20000)
# print(Student.salary)


# #student class
# class Student:
#     college = "Bennett"
#     def __init__(self, name,age, course):
#         self.name=name
#         self.age= age
#         self.course= course

#     def display(self):
#         print(self.name)
#         print(self.age)
#         print(self.course)

#     @classmethod
#     def change_college(cls, newname):
#         cls.college= newname

#     @staticmethod
#     def greet():
#         print("This is a student class")
#         return 20 #without return it print none because it is not returning anything

# s1= Student("Askara","20","B.Tech")
# s1.display()
# Student.change_college("IIT")
# print(Student.college)
# print(Student.greet())  


#Car class
class Car:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model= model
        self.price=price

    def car_info(self):
        print(self.brand)
        print(self.model)
        print(self.price)

car1=Car("Mercidies","S-Class", 100000)
car2= Car("BMW","X5", 80000)
car1.car_info()
car2.car_info()
print(car1.brand)