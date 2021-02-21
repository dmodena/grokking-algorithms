import unittest
from algorithms.tailrecursion.sum import sum

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([1, 2, 3, 4, 5, 6]), 21)
