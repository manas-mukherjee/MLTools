from random import randint
from cProfile import Profile
from pstats import Stats

def insertion_sort(data):
    result = []
    for value in data:
        # print(value)
        insert_value(result, value)
    return result

def insert_value(array, value):
    for i, existing in enumerate(array):
        if existing > value:
            array.insert(i, value)
            return
    array.append(value)

max_size = 10**4
data = [ randint(0, max_size) for _ in range(10)]
print(data)

# result = insertion_sort(data)
# print(result)

profiler = Profile()
profiler.runcall(lambda : insertion_sort(data))
print('Done')

stats = Stats(profiler)
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats()
stats.print_callers()