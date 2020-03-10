# Debugging - https://www.safaribooksonline.com/videos/effective-python/9780134175249/9780134175249-EPLL_06_03

def atest(a, b):
    print('This is a test function')
    import pdb; pdb.set_trace()
    c = a / b
    print(c)


if __name__ == '__main__':
    atest(10, 0)
