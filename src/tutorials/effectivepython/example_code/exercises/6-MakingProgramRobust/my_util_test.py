#my_util_test.py
#preamble

from unittest import TestCase, main
from my_util import calculator

class ClassName(TestCase):
    """docstring for ."""

    def test_calculator(self):
        self.assertEqual(5, calculator(2,3,'add'))

if __name__ == '__main__':
    main()
