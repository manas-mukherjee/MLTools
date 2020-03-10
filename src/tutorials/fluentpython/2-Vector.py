#Example 1-2 is a Vector class implementing the operations just described, through the use of the special methods __repr__, __abs__, __add__ and __mul__.
from math import hypot

class Vector:
    """docstring for Vector."""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    def __mul__(arg):
        x = self.x * other.x
        y = self.y * other.y
        return Vector(x,y)

print(Vector(3,4))
#print(Vector('3','4'))
print(bool(Vector(3,4)))
print(Vector(1,2) + Vector(3,4) )
