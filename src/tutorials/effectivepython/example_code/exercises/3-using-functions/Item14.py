#Item 14
#Accept functions for simple interfaces instead of classes
# used for callback
#Ex1
names = ['Sachin', 'Saurabh', 'Lara','Imran']
names.sort(key=lambda x: len(x))
print(names)

#Ex2 (change the behaviour of the default dict class)
from collections import defaultdict
d = defaultdict(lambda: 100)
d['foo'] = 55
print(d['foo'])
print(d['bar'])

#supplying function
def log_missing():
    print('Key added')
    return 0

d = defaultdict(log_missing)
d['foo'] = 55
print(d['foo'])
print(d['bar'])
print(d)

# count how many times the key was missing
print('increment_with_report')
def increment_with_report(current, increments):
    added_count = 0

    #statefull function
    def missing():
        nonlocal added_count
        added_count+=1
        return 0

    result = defaultdict(missing, current)
    for key, offset in increments:
        result[key] += offset

    return result, added_count

current = {'green':12, 'blue':3}
increments = [('red', 5), ('blue', 17), ('orange',9)]
print(increment_with_report(current, increments))

#Statefull closures
print('CountMissing\n-------------\n')
class CountMissing(object):
    """docstring for CountMissing."""
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0

counter = CountMissing()
#print(callable(counter))

current = {'green':12, 'blue':3}
result = defaultdict(counter, current)

increments = [('red', 5), ('blue', 17), ('orange',9)]
for key, offset in increments:
    result[key] += offset

print(counter.added)
