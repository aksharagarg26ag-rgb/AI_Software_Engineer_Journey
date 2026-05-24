#Function to print hello.
def hey():
    return "hello"
print(hey())

#Function to add two numbers.
def add(a,b):
    return a+ b
print(add(4,5))

#Function to find square.
def square(num):
    return num*num
print(square(4))

#Function to check even/odd.
def even_odd(num):
    if (num%2 == 0):
        return " even"
    else:
        return "odd"
print(even_odd(4))

#Function for factorial.
def fact(num):
    if num==1 or num ==0:
        return 1
    else:
        return num * fact(num-1)
print(fact(5))

#Function for prime check.
def prime(num):
    if num < 2:
        return "Not prime"
    for i in range(2, num):
        if num % i == 0:
            return "Not prime"
    return "Prime"

print(prime(6))

#Function to reverse string
def reverse(num):
    rev=0
    while num>0:
        rev = rev*10 + num % 10
        num = num //10
    return rev
    
print(reverse(1234))

#Function to find largest in list.
def largest(num):
    num.sort()
    return num[-1]
print(largest([2,4,6,8,10]))