#Item 11
#Consider generators instead of returning lists

def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result

str = '''He as compliment unreserved projecting. Between had
observe pretend delight for believe. Do newspaper questions
consulted sweetness do. Our sportsman his unwilling fulfilled
departure law. Now world own total saved above her cause table.
Wicket myself her square remark the should far secure sex.
Smiling cousins warrant law explain for whether. '''

result = index_words(str)
print(result[:10])


## Rewrite the function using generator ( instead of list)
# easier to read. 'yeild' makes it clear on what is being returned.
# It can handle any amount of the data
def index_words_generator(text):
    result = []
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1
    return result

result = index_words_generator(str)
for i in range(10):
    print(next(result))

# stream of data
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
    print(next(result))
    print(next(result))
    print(next(result))
