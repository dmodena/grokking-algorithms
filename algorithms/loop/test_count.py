import unittest
from algorithms.loop.count import count

class TestCount(unittest.TestCase):
    def test_count(self):
        self.assertEqual(count([]), 0)
        self.assertEqual(count([1, 2, 3, 4]), 4)
        self.assertEqual(count([1, 2, 3, 4, 5, 6]), 6)
        self.assertEqual(count([1, 2, 3, 4, 5, 6, 7, 8]), 8)
