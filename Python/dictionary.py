dict={
    "name":"Akshara",
    "age":"20",
    "year": "2nd",
    "University":"Bennett University"
}
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get("University"))

 #Count frequency of characters in string.
text= {"Akshara"}
freq={}
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:

        freq[ch] = 1
print(freq) 

