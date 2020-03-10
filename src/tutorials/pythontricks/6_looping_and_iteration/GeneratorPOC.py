def repeater(value):
    while True:
        yield value
        value += 10
        print(10)


next(repeater(10))
next(repeater(15))