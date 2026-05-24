#Create list of: ,numbers 1–10 ,squares ,cubes
nums=[i for i in range(10)]
print(nums)
square=[i*i for i in range(5)]
print(square)
cubes=[i*i*i for i in range(5)]
print(cubes)

#Create even/0dd number list.
num=[ i for i in range(10) if i%2==0]
print(num)
odd=[i for i in range(10) if i%2 !=0]
print(odd)

#Convert strings to uppercase.
strs=["hello","world"]
upper=[s.upper() for s in strs] 
print(upper)

#Numbers divisible by 3.
num=[i for i in range(10) if i%3==0]
print(num)

#Remove negative numbers
num= [1,4,-5,6,-7]
nums=[i for i in num if i>0]
print(nums)

#Extract vowels from string.
string="hello"
vowel=[ ch for ch in string if ch in "aeiouAEIOU"]
print(vowel)

#Flatten matrix:
matrix=[[1,2,3],[4,5,6],[7,8,9]]
flat=[num for row in matrix for num in row]
print(flat)

#Create multiplication table list.
num=4
table=[num * i for i in range(1, 10)]
print(table)

#Find common elements between lists.
lis=[1,3,2,4,24]
common= [i for i in lis if i in lis]
print(common)

