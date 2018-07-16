#Item2 : Avoid using start, end, and stride in a single slice
# somelist [ start, end, strid ]
# start:inclusive, end:exclusive

a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

#even index
print(a[::2])

#odd index
print(a[1::2])

#byte string ( Imp )
x = b'mongoose'
y = x[::-1]
print(y)

#Works well with byte and ascii
#but breaks for unicode character encoded using utf-8

#Negative stride
a = ['a','b','c','d','e','f','g','h']
print(a[::-2])
print(a[-2::-2])
print(a[-2:2:-2])

#strid first and then do slice
b = a[::2]
c = b[1:-1]
print(a)
print(b)
print(c)