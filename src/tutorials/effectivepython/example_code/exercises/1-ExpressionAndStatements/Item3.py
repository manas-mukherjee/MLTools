# Instead of range use enumerate

from random import randint

#range, bin function
random_bits = 0
print(str(bin(11)))

#enum
a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
for i, color in enumerate(a,1):
    print("%d: %s is a nice color" % (i, color))

#enumerate(a) : lazy generator
print(list(enumerate(a,1)))

