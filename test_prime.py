import unittest

from prime_number import is_prime

# class TestClass(unittest.TestCase):
#     def test_prime_not_prime(self):
#         self.assertTrue(is_prime(2))
#         self.assertTrue(is_prime(5))
#         self.assertTrue(is_prime(9))
#         self.assertTrue(is_prime(11))

class TestPrime(unittest.TestCase):
    def test_1(self):
        self.assertTrue(is_prime(2))
    def test_2(self):
        self.assertTrue(is_prime(5))
    def test_3(self):
        self.assertFalse(is_prime(9))
    def test_4(self):
        self.assertTrue(is_prime(11))

if __name__ == '__main__':
    unittest.main()