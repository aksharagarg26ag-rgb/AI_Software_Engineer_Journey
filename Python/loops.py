#Print numbers: 1 to 100
for i in range(1,100):
    print(i)

#odd number
for i in range(1,100,2):
    print(i)

#even number
for i in range(2,100,2):
    print(i)

#Print multiplication table.
num=4
for i in range(1,10):
    print(num * i)

#Find:sum of numbers
nums=[2,4,2,6,8]
sum=0;
for i in range(len(nums)):
    sum += nums[i]
print(sum)

#factorial
nums=[2,4,2,6,8]
fact=0
for i in range(len(nums)):
    fact *= nums[i]
print(fact)

#reverse counting
nums=[2,4,2,6,8]
for i in range(len(nums)-1,-1,-1):
    print(nums[i])  

#Prime number check
num= int(input())
for i in range(2,num):
    if num % i == 0:
        print("Not prime")
        break
else:
    print("Prime")

#Fibonacci series
n=int(input())
a, b = 0, 1
for _ in range(n):
    print (a)
    a,b = b, (a+b)

#Reverse a number
num=int(input())
rev = 0
while num > 0:
    rev = rev*10 + num % 10
    num = num // 10  
    print(rev)

#Palindrome number
num=int(input())
rev=0
nums = num
while nums> 0:
    rev = rev *10 + nums % 10
    nums = nums // 10

if rev == num:
    print("Palindrome")
else:
    print("Not Palindrome")


# count digit in number
num=int(input())
count = 0
while num > 0:
    num = num // 10
    count += 1  
print(count)    

#Sum of digits
num= int(input())
sum = 0
while num> 0:
    sum+= num % 10
    num = num // 10

print(sum)

#Pattern questions
n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*", end="") #prevents automatic newline.
    print() #next line

num= int(input())
for i in range(num):
    for j in range( i+1):
        print(j+1, end="")
    print()
