list=[1,2,3,4,2,6,7,8,9,10]
#remove duplicates
unique =[]
for i in list:
    if i not in unique:
        unique.append(i)
    else:
        i+=1
print (unique)

#sort
print(list.sort())