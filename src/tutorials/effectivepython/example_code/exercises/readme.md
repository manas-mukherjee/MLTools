Training  - https://www.safaribooksonline.com/videos/effective-python

## 2-List Comprehension and Generators

### 1. List Comprehension ( Ref - Item 9)
```
a = list(range(100))
print(a)
b = [x for x in a if x%2==0 and x%3==0]
print(b)
b = [x**2 for x in a if x%2==0]
print(b)
b = [x**2 for row in matrix for x in row]
print(b)
```

### 2. Generator ( Ref - Item 11)
```
print('stream file data')
def index_words_file(handle):
    offset = 0
    for line in handle:
        if line:
             yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset

with open('./2-Comprehensions-Generators/item11.txt', 'w') as f:
    f.write(str)
with open('./2-Comprehensions-Generators/item11.txt') as f:
    result = index_words_file(f)
    #print(list(result))
    print(next(result))
```