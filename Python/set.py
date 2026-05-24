#Remove duplicates using set.
sets = {1, 2,2, 3, 4}
print(sets)

#Find common elements between two lists.
l1= {1, 2, 3, 4, 5}
l2={3, 4, 5, 6, 7}
print(l1.intersection(l2))
print(l1.difference(l2))
print(l1.union(l2))

#Find unique elements.
a=l1.union(l2)
b=l1.intersection(l2)
print(a.difference(b))