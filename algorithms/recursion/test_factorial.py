import unittest
from algorithms.recursion.factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(8), 40_320)
