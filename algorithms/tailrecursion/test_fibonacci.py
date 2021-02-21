import unittest
from algorithms.tailrecursion.fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 1)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 2)
        self.assertEqual(fibonacci(3), 3)
        self.assertEqual(fibonacci(4), 5)
        self.assertEqual(fibonacci(5), 8)
        self.assertEqual(fibonacci(6), 13)
        self.assertEqual(fibonacci(7), 21)
