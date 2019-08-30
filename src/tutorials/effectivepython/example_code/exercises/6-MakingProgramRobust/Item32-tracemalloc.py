import os
import hashlib

class MyObject(object):
    def __init__(self):
        self.x = os.urandom(100)
        self.y - hashlib.sha1(self.x).hexdigest()

def get_data():
    values = []
    for _ in range(100):
        obj = MyObject()
        values.append(obj)
    return values_str

def run():
    deep_values = []
    for _ in range(100):
        deep_values.append(get_data())
    return deep_values

import gc

found_objects = gc.get_objects()
print('%d object before ' % len(found_objects))

import waste_memory
x = waster_memory.run()

found_objects = gc.get_objects()
print('%d object before ' % len(found_objects))
