'''
Container sequences
list, tuple, and collections.deque can hold items of different types.
Flat sequences
str, bytes, bytearray, memoryview, and array.array hold items of one type.'''

symbols = '$¢£¥€¤'

codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)

codes = [ord(symbol) for symbol in symbols]
print(codes)

a, b , *rest = range(5)
print(rest)
l = range(5)
print(type(l))

a, *body, c, d = range(5)
for i in range(5):
    print(i)
