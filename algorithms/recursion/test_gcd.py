import unittest
from algorithms.recursion.gcd import euclidean, factorization

class TestGCD(unittest.TestCase):
    def test_euclidean(self):
        self.assertEqual(euclidean(2322, 654), 6)
        self.assertEqual(euclidean(654, 2322), 6)
        self.assertEqual(euclidean(888, 54), 6)
        self.assertEqual(euclidean(240, 30), 30)
        self.assertEqual(euclidean(81, 7), 1)

    def test_factorization(self):
        self.assertEqual(factorization(2322, 654), 6)
        self.assertEqual(factorization(654, 2322), 6)
        self.assertEqual(factorization(888, 54), 6)
        self.assertEqual(factorization(240, 30), 30)
        self.assertEqual(factorization(81, 7), 1)

    def test_equivalent(self):
        self.assertEqual(euclidean(2322, 654), factorization(2322, 654))
