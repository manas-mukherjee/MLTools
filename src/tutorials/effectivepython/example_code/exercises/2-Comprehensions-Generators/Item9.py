#Item 9 Avoid more than two expressions in list comprehensions

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)


#flattening using multiple loops
flat = [x for row in matrix for x in row]
print(flat)

squared = [[x**2 for x in row] for row in matrix]
print(squared)

#3d matrix
mat = [
    [[1,2,3],[4,5,6]],
    [[7,8,9],[10,11,12]]
]
print("3d", mat)

li = []
for sub1 in mat:
    for sub2 in sub1:
        li.extend(sub2)
print(li)

''' Difference between append and extend '''
x  = [1,2,3]
y  = [4,5]
x.append(y)
print(x)

x  = [1,2,3]
y  = [4,5]
print(x.extend(y))
print(x)
##################

a = [1,2,3,4,5,6,7,8,9,10]
print(a)
b = [x for x in a if x>4 and x%2==0]
c = [x for x in a if x>4 if x%2==0]
assert b==c
##################
# not right approach
print(matrix)
filtered = [[x for x in row if x%3==0] for row in matrix if sum(row) > 10 ]
print(filtered)

##################
# avoid more than 2 expressions in a single expressions

a = list(range(100))
b = [ x for x in a if x%2==0 if x%3==0]
print(b)
##################

print(matrix)
mat_sqr = [x**2 for row in matrix for x in row]
print(mat_sqr)
##################

print(a)
#1
b = [x for x in a if x%2==0 and x%3==0]
print(b)
b = [x**2 for x in a if x%2==0]
print(b)
b = [x**2 for row in matrix for x in row]
print(b)
