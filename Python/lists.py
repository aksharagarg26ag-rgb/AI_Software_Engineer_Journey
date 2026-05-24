#Take 10 numbers from user and store in list.
numbers=[]
for i in range(10):
    value= int(input())
    numbers.append(value)

print(numbers)
 #even numbers odd numbers
for i in range(10):
    val= int(numbers[i]) % 2
    if val == 0:
        print ("even")
    else:
        print("odd")
#sum
val = 0
for i in range(10):
    
    val += numbers[i]
print(val)
#average
print(val/10)

# second largest number
for i in range(10):
    numbers.sort()
print(numbers[-2])
 
 #bubble sort
for i in range(10):
    for j in range(9):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print(numbers)

#remove duplicates
unique= []
for i in numbers:
    if i not in unique:
        unique.append(i)
print(unique)