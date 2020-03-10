class OldRegister(object):
    """docstring for OldRegister."""
    def __init__(self, ohms):
        self._ohms = ohms

    def get_ohms(self):
        return self._ohms

    def set_ohms(self, ohms):
        self._ohms = ohms

r0 = OldRegister(50e3)
r0.set_ohms(r0.get_ohms() + 5e3)
print('Resistence is %f' % r0.ohms)
