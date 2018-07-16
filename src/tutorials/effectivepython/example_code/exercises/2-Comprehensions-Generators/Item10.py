#Item 10
#Consider generator expressions for large comprehensions
import random

#generator expressions
with open('./my_file.txt', 'w') as f:
    for _ in range(10):
        f.write('a' * random.randint(0,100))
        f.write('\n')

#inefficient for large and/or continuous input
value = [len(x) for x in open('./my_file.txt')]
print(value)

#generator(returns iterator)
value = (len(x) for x in open('./my_file.txt'))
print(value) # <generator object <genexpr> at 0x10ee0c888>
# Doesn't blow up the memory
print(next(value))

#lazy iternation using generator 
roots = ((x, x**0.5) for x in value)
print(next(roots))
print(next(roots))
print(next(roots))
print(next(roots))
