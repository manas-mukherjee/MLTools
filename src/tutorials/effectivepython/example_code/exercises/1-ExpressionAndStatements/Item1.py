# Know how to slice sequences

a = ['a','b','c','d','e','f','g','h']

#First 4 items
print(a[:4])

#Last 4 items
print(a[-4:])
print(a[4:])

#Interior items
print(a[3:-3])
print(a[5:len(a)])
print(a[:-1])
print(a[-3:-1])

print(a[:30])

#Slice assignment
b, c = a[3:-3]
print(b,c)
#Fail
#b, c = a[:3]
#print(b,c)

#Splice ( truncate, size is different )
print(a[2:7])
a[2:7] = [99,100,101]
print(a)

#Copy of a list
b = a[:]
print(a)
print(b)
print(id(a))
print(id(b))
assert a == b
assert a is not b

#Caution( negative value in slicing )
#Negative 0 means all items
n = 0
print(a[-n:])
