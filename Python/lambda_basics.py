square = lambda x: x*x
print(square(5))

add= lambda a,b: a+b
print(add(2,3))

even_odd= lambda x: "even" if x%2==0 else "odd"
print(even_odd(4))

#LAMBDA WITH map()
numbers = [1,2,3,4,5]
square= list(map(lambda x: x*x, numbers))
print(square)

string=["i" , "am " , "Akshara"]
uppercase= list(map(lambda s: s.upper(), string))
print(uppercase)

string=["1", "2", "3"]
integer= list(map(lambda s: int(s), string))
print(integer)


#LAMBDA WITH FILTER
lis=[1,2,3,4,5,6,7,8,9]
even= list(filter(lambda x: x%2 ==0, lis))
print(even)

lis=[1,2,3,-4,-5,-6,7,8,9]
even= list(filter(lambda x: x>0, lis))
print(even)

str= ["akshara", "garg", "bennett"]
charact=list(filter(lambda s: len(s)>5, str))
print(charact)
             

#LAMBDA WITH SORTING
employees = [("A",50000),("B",30000)]
sorted_employees= sorted(employees, key=lambda x: x[1])
print(sorted_employees)