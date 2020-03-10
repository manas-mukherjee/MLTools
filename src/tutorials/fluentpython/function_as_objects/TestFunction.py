##############################################
# Treating a Function Like an Object         #
##############################################

# Example 5-1
print('\nExample 5-1\n------------\n')
def factorial(n):
    '''Returns n factorial'''
    return 1 if n<2 else n * factorial(n-1)

print(factorial(42))

print(factorial.__doc__)
print(type(factorial))
print(help(factorial))

# Example 5-2
print('\nExample 5-2\n------------\n')
fact = factorial
print(fact(6))

print(list(map(fact, range(10))))

# Example 5-3
print('\nExample 5-3\n------------\n')
# Higher order functions
# Imp: map, filter, and reduce
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len, reverse=True))

# Example 5-4
print('\nExample 5-4\n------------\n')
def reverse(word):
    return word[::-1]

print(sorted(map(reverse, fruits), key=len))

# Example 5-5
print('\nExample 5-5\n------------\n')
# A listcomp or a genexp does the job of map and filter combined, but is more readable.

#Old way using list - Build a list of factorials from 0! to 5!.
print(list(map(fact, range(6))))
#New way using list comprehension.
print([fact(num) for num in range(6)])

#Old way using list - List of factorials of odd numbers up to 5!, using both map and filter..
print(list(map(fact, filter(lambda n : n%2, range(6)))))
#New way using list comprehension.
print([fact(num) for num in range(6) if num % 2])

# Example 5-6
print('\nExample 5-6\n------------\n')
#Starting with Python 3.0, reduce is not a built-in.
from functools import reduce
from operator import add
print(reduce(add, range(100)))
print(sum(range(100)))

l = [n for n in range(25) if n % 2 == 0]
print(l)
print(all(l[1:]))
print(any([1,0,0,0]))


##############################################
# Anonymous Functions                        #
##############################################

# Example 5-7
print('\nExample 5-6\n------------\n')

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=reverse))
print(sorted(fruits, key = lambda x : x[::-1]))

##############################################
# User-Defined Callable Types                #
##############################################
# Example 5-8
print('\nExample 5-8\n------------\n')

import random

class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BignoCase')

    def __call__(self, *args, **kwargs):
        return self.pick()

bingo = BingoCage(range(3))
print("direct - " , bingo())

for i in range(2):
    p = bingo.pick()
    print(p)


# for l in dir(factorial):
#     print(l)

print(factorial.__dict__)

import bobo
