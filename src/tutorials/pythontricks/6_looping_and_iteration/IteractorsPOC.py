# Concept1
# class RepeaterIteractor(object):
#     def __init__(self, source):
#         self.source = source
#
#     def __next__(self):
#         return self.source.value
#
# class Repeater:
#     def __init__(self, value):
#         self.value = value
#
#     def __iter__(self):
#         return RepeaterIteractor(self)
#
# repeater = Repeater('Hello')
#
# for item in repeater:
#     print(item)

# Concept2
# iterator = repeater.__iter__() # iteractor = iter(repeater)
# while True:
#     item = iterator.__next__() # next(iteractor)
#     print(item)

# Concept3
# __next__ within Repeater. No need for RepeaterIteractor

# class Repeater:
#     def __init__(self, value):
#         self.value = value
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         return self.value
#
# repeater = Repeater('Hello')
#
# for item in repeater:
#     print(item)

# Concept4 [ Bounded iteractor ]
# my_list = [1,2,3]
# iteractor = iter(my_list)
#
# print(next(iteractor))
# print(next(iteractor))
# print(next(iteractor))
# print(next(iteractor)) # Raise a StopIteration exception


# Concept5 [ Bounded iteractor ]
# class BoundedRepeater:
#     def __init__(self, value, max_repeats):
#         self.value = value
#         self.max_repeats = max_repeats
#         self.count = 0
#
#     def __iter__(self):
#         return self
# 
#     def __next__(self):
#         if self.count >= self.max_repeats:
#             raise StopIteration
#         self.count += 1
#         return self.value
#
# repeater = BoundedRepeater('Hello', 3)
# for item in repeater:
#     print(item)
#
# iterator = BoundedRepeater('Hello', 3).__iter__()
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))