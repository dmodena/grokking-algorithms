import unittest
from algorithms.loop.select_sort import select_sort, get_lowest_index

class TestSelectSort(unittest.TestCase):
    def test_select_sort(self):
        self.assertEqual(select_sort([5, 3, 6, 2, 10]), [2, 3, 5, 6, 10])
        self.assertEqual(select_sort([5, 2]), [2, 5])
        self.assertEqual(select_sort([3]), [3])
        self.assertEqual(select_sort([]), [])

    def test_get_lowest_index(self):
        self.assertEqual(get_lowest_index([5, 3, 6, 2, 10]), 3)
        self.assertEqual(get_lowest_index([5, 3, 6, 10]), 1)
        self.assertEqual(get_lowest_index([5, 6, 10]), 0)
        self.assertEqual(get_lowest_index([10]), 0)
        self.assertEqual(get_lowest_index([]), None)
