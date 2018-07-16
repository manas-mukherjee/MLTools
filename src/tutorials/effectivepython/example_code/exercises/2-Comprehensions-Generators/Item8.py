# Item 8
# Use list comprehensions instead of MAP and FILTER

a = [ 1,2,3,4,5,6,7,8,9,10]
print(a)

# List comprehension
squares = [x**2 for x in a]
print(squares)

# Using map function
squares1 = map(lambda x : x**2, a)
#print(type(squares1)) -- <class 'map'>
print(list(squares1))

# List comprehension with filtering
squares2 = [x**2 for x in a if x%2==0]
print(squares2)

# List comprehension using map
squares3 = map(lambda x : x**2, filter(lambda y : y%2==0, a))
print(list(squares3))

#dictionary
countries = {'Coratia':1, 'Germany':2, 'Argentina':3}
rank_country = {rank: name for name, rank, in countries.items()}
print(rank_country)

#set
countries_set_len = {len(x) for x in countries.keys()}
print(type(countries_set_len))
print(countries_set_len)
