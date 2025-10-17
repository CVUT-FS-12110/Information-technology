# test_math_utils.py

import unittest
from math_server import factorial, is_prime

class TestFactorial(unittest.TestCase):
    def test_factorial_basic(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)

    def test_factorial_large(self):
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_type_error(self):
        with self.assertRaises(TypeError):
            factorial(3.5)
        with self.assertRaises(TypeError):
            factorial("5")

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)


class TestIsPrime(unittest.TestCase):
    def test_small_primes(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(13))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(0))

    def test_composites(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(15))

    def test_large_prime(self):
        self.assertTrue(is_prime(97))
        self.assertFalse(is_prime(100))

    def test_type_error(self):
        with self.assertRaises(TypeError):
            is_prime(3.14)
        with self.assertRaises(TypeError):
            is_prime("11")


if __name__ == "__main__":
    unittest.main(verbosity=2)
