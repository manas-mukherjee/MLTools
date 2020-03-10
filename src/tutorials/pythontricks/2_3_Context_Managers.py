with open('hello.txt', 'w') as f:
    f.write('I am the wolf climbing the hill')

class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print("__enter__")
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")
        if self.file:
            self.file.close()

with ManagedFile('world.txt') as f:
    f.write("this is a new science world!")