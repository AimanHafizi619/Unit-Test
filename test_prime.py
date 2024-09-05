import unittest

from prime_number import is_prime
from mix_number import add

class TestPrime(unittest.TestCase):

    def test_prime_not_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(9))
        self.assertTrue(is_prime(11))

    # def test_1(self):
    #     self.assertTrue(is_prime(2))
    # def test_2(self):
    #     self.assertTrue(is_prime(5))
    # def test_3(self):
    #     self.assertFalse(is_prime(9))
    # def test_4(self):
    #     self.assertTrue(is_prime(11))

    def test_exception(self):
        self.assertRaises(TypeError,is_prime,"five")
        self.assertRaises(TypeError,is_prime,7.0)
        self.assertRaises(TypeError,is_prime,"five")

    # def test_type_error1(self):
    #     with self.assertRaises(TypeError):
    #         is_prime("five")
    # def test_type_error2(self):
    #     with self.assertRaises(TypeError):
    #         is_prime(7.0)
    # def test_value_error(self):
    #     with self.assertRaises(ValueError):
    #         is_prime(-11)

    def test_add_function(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, -2), -3)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-1, 2), 1)

    # def test_add_pos_num(self):
    #     self.assertEqual(add(1, 2), 3)
    # def test_add_neg_num(self):
    #     self.assertEqual(add(-1, -2), -3)
    # def test_add_zero(self):
    #     self.assertEqual(add(0, 0), 0)
    # def test_mix_num(self):
    #     self.assertEqual(add(-1, 2), 1)

if __name__ == '__main__':
    unittest.main()

# python -m unittest test_prime.py --> Just show the result
# python test_prime.py -v --> show results of each function