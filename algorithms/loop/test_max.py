import unittest
from algorithms.loop.max import max

class TestMax(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max([1, 2, 3]), 3)
        self.assertEqual(max([3, 6, 9, 12]), 12)
        self.assertEqual(max([8, 6, 4, 2]), 8)
        self.assertEqual(max([10, 5, 25, 50, 15]), 50)
