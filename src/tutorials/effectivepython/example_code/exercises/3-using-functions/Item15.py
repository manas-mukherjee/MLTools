# Item 15
# Reduce visual noise with variable positional arguments
def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))

log('My numbers are', [1,2])
log('My numbers 2') #passing the 2nd arg : empty list

favourites = [7, 33, 99]
log('My favourites are ', *favourites)
log('My favourites are ', 7,33,99)

#passing a generator
def my_gen():
    for i in range(10):
        yield i
log('Hi there', *my_gen()) # generated gets converted to a tuple here
# '*' args work with limited number of arguments
# with '*' args, new param can't be added
