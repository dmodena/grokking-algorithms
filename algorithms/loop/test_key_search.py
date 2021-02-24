import unittest
from algorithms.loop.key_search import Box, Key, key_search

class TestKeySearch(unittest.TestCase):
    def create_complex_pile(self):
        a = Box()
        b1 = Box()
        b2 = Box()
        b3 = Box()
        b4 = Box()
        c11 = Box()
        c12 = Box()
        c13 = Box()
        c14 = Box()
        c21 = Box()
        c22 = Box()
        c23 = Box()
        c31 = Box()
        c41 = Box()
        c42 = Box()
        d111 = Box()
        d112 = Box()
        d121 = Box()
        d122 = Box()
        d221 = Box()
        d222 = Box()
        d411 = Box()
        d412 = Box()
        e1111 = Box()
        e1112 = Box()
        e1113 = Box()
        e2221 = Box()

        d111.items = [e1111, e1112, e1113]
        d222.items = [e2221]

        c11.items = [d111, d112]
        c12.items = [d121, d122]
        c22.items = [d221, d222]
        c41.items = [d411, d412]
        c42.items = [Key()]

        b1.items = [c11, c12, c13, c14]
        b2.items = [c21, c22, c23]
        b3.items = [c31]
        b4.items = [c41, c42]

        a.items = [b1, b2, b3, b4]

        return a

    def create_simple_pile(self):
        b1 = Box()
        b2 = Box()
        b3 = Box()
        b4 = Box()
        b5 = Box()
        b6 = Box()
        b7 = Box()

        b6.items = [Key()]
        b5.items = [b6, b7]
        b2.items = [b3, b4]
        b1.items = [b2, b5]

        return b1

    def create_no_key_pile(self):
        b1 = Box()
        b2 = Box()
        b3 = Box()
        b4 = Box()

        b1.items = [b2, b3, b4]

        return b1

    def create_empty_box(self):
        return Box()


    def test_key_search(self):
        test_complex_pile = self.create_complex_pile()
        test_simple_pile = self.create_simple_pile()
        test_no_key_pile = self.create_no_key_pile()
        test_empty_box = self.create_empty_box()

        self.assertEqual(key_search(test_complex_pile), 'key')
        self.assertEqual(key_search(test_simple_pile), 'key')
        self.assertEqual(key_search(test_no_key_pile), None)
        self.assertEqual(key_search(test_empty_box), None)
