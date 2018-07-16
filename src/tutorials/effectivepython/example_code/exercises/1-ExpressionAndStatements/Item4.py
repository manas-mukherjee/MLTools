#Item4 : Use zip to process iterators in parallel
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
letters = [len(n) for n in colors]

for i, j in zip(colors, letters):
    print(i,j)

print(list(zip(colors, letters)))

'''
Python2 Zip doesn't generate a lazy copy. Alternative [from itertools import izip]
Python3 produces a lazy zip object

Zip doesn't work if input iterators are of different lengths.
it only works till matching index position. Alternative solution [ from itertools import zip_longest ]
'''

from itertools import zip_longest

colors.append('black')
print(colors)
for i, j in zip_longest(colors, letters):
    print(i,j)