#Item 12
#Be defensive when iterating over arguments

data = [15,80,35]

def normalize(numbers):
    total = sum(numbers) # iternation 1
    result = []

    for value in numbers: # iternation 2
        perc = 100*(value/total)
        result.append(perc)
    return result

output = normalize(data)
print(output)
print(sum(output))

#scale the data : read the input from a file.
#leverage generator

path = './2-Comprehensions-Generators/item12.txt'
with open(path, 'w') as f:
    for i in data:
        f.write('%d\n' % i)

def read_visits_Gen(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)

result = read_visits_Gen(path)
print(list(result))
print(list(result)) #list will not iterate again

get_iter = lambda: read_visits_Gen(path)
print(get_iter())
print(sum(get_iter()))

#pythonic way
print('pythonic way\n-----------')
a = [1,2,3,4,5]
for x in a:
    print(x)

it = iter(a)
it = a.__iter__() #equivalent to above
value = next(it)
value = it.__next___()
