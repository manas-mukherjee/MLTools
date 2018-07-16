#Item7: Consider CONTEXTLIB and with statements for reusable Try/finally behaviour
from threading import Lock

lock = Lock()

with lock:
    print("Lock is held")


lock.acquire()
try:
    print('Lock is also held')
finally:
    print('Lock released')
    lock.release()

#---------------

import logging
logging.getLogger().setLevel(logging.WARNING)

def my_function():
    logging.debug("this is debug")
    logging.error("this is error")
    logging.debug("this is another debug")

#---------------temporarily elevate the logging level
from contextlib import contextmanager

@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)

    try:
        yield
    finally:
        logger.setLevel(old_level)

with debug_logging(logging.DEBUG):
    my_function()

my_function()

#Swallow exceptions
@contextmanager
def swallow_exception(cls):
    try:
        yield
    except cls:
        logging.exception(':::Swallowing exception')
value = 20
with swallow_exception(ZeroDivisionError):
    value /=0
print('Done')