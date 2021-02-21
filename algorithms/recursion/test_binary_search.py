import unittest
from algorithms.recursion.binary_search import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 3), 3)
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 5), 5)
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 9), 9)
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 8), None)
        self.assertEqual(binary_search([1, 3, 5, 7, 9], -1), None)
