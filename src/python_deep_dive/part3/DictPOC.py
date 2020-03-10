from collections import defaultdict

# d = defaultdict(lambda : "python")
# print(d['a'])
# print(d)
#
# dint = defaultdict(lambda : 0)
# print(dint['a'])
# print(dint)
#

#here int is not a type, it works as a callable
dint1 = defaultdict(int)
print(dint1['a'])
print(dint1)

# dint1 = defaultdict(list)
# print(dint1['a'])
# print(dint1)

counts = {}
sentence = "Life is beautiful"

for c in sentence.lower():
    if c in counts:
        counts[c] += 1
    else:
        counts[c] = 1

print(counts)

# Alternative
counts_dd = defaultdict(lambda : 0)

for c in sentence.lower():
    counts_dd[c] += 1

print(counts_dd)

print(isinstance(counts_dd, defaultdict))
print(counts_dd.keys())
print(counts_dd.values())
print(counts_dd.items())


# example usage
'''
persons = {
    "Manas": defaultdict(lambda : "Unknown", age=33, eye_color="brown"),
    "William": defaultdict(lambda : "Unknown", eye_color="blue"),
    "Robot": defaultdict(lambda : "Unknown", age=33)
}


eye_colros = defaultdict(list)
for name, desc in persons.items():
    print(name, desc["age"], desc["eye_color"])
    eye_colros[desc['eye_color']].append(name)

print(eye_colros)
'''

# Alternative
'''
from functools import partial

eyedict = partial(defaultdict, lambda : 'unknown')

persons = {
    "Manas": eyedict(age=33, eye_color="brown"),
    "William": eyedict(eye_color="blue"),
    "Jarred": eyedict(eye_color="blue"),
    "Robot": eyedict(age=33)
}

eye_colros = defaultdict(list)
for name, desc in persons.items():
    print(name, desc["age"], desc["eye_color"])
    eye_colros[desc['eye_color']].append(name)

print(eye_colros)
'''

# Another usage
from collections import defaultdict, namedtuple
from datetime import datetime
from functools import wraps

def function_stats():
    d = defaultdict(lambda: {"count": 0, "first_called": datetime.utcnow()})
    Stats = namedtuple('Stats', 'decorator data')

    # Decorator function
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            d[fn.__name__]['count'] += 1
            return fn(*args, **kwargs)
        return wrapper

    return Stats(decorator, d)

stats = function_stats()
print(stats.decorator)
print(stats.data)

@stats.decorator
def func_1():
    pass

@stats.decorator
def func_2(x, y):
    pass

func_1()
print(stats.data)

func_1()
print(stats.data)

func_2(1,2)
print(stats.data)