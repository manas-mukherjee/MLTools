#Item 13
#Know how closures interact with variable scope

numbers = [8,3,1,2,5,4,7,6]
group = {2,3,5,7} # Higher priority

def helper(x):
    if x in group:
        return (0,x) # tuple comparison ( 0 will come before 1 item while doing the comparision)
    return (1,x)

numbers.sort(key=helper)
print(numbers)

# closures
# helper will carry a ref to the group which is defined in the outer scope
# in python, function is considered as first class variable
print('sort_priority\n----------------\n')

def sort_priority(numbers, group):
    found = False
    def helper(x):
        if x in group:
            found = True # why it didn't work ?
            return (0,x) # tuple comparison ( 0 will come before 1 item while doing the comparision)
        return (1,x)

    numbers.sort(key=helper)
    return found

ret = sort_priority(numbers, group)
print(ret)
print(numbers)



# how closures interact with variable scope
print('how closures interact with variable scope\n')
def enclosing():
    foo = 15
    foo = 25

    def my_func():
        foo = 10
        bar = 5
        print(foo)
        print(bar)

    my_func()
    print(foo)
    #print(bar)

enclosing()


# How to handle it
# Python non local variable(available in python 3 only)

print('Sorter using class\n-------------------------')
class Sorter(object):
    """docstring for Sorter."""
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0,x)
        return (1,x)

sorter = Sorter(group)
numbers.sort(key=sorter)
print(sorter.found)
print(numbers)
