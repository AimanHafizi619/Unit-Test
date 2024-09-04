import unittest

class TestString(unittest.TestCase):

    def test_string_a(self):
        self.assertEqual('a'*5, 'aaaaa')
    
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    
    def test_isupper(self):
        self.assertTrue('MOO'.isupper())
        self.assertFalse('Moo'.isupper())

    def test_strip(self):
        self.assertEqual('  hello  '.strip(), 'hello')
        self.assertEqual('monster'.strip('mon'), 'ster')

    def test_split(self):
        word = 'hello world'
        self.assertEqual(word.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            word.split(2)  

class TestStringMethod(unittest.TestCase):

    def test_neg_string(self):
        key = "love"
        container = "clover"
        # Error message in case test case failed
        message = "The key is not in the container"
        self.assertIn(key, container, message)

    def test_pos_string(self):
        key = "clvr"
        container = "clover"
        # Error message in case test case failed
        message = "The key is in the container"
        self.assertNotIn(key, container, message)

class TestNoneValue(unittest.TestCase):

    def test_not_none_value(self):
        firstValue = 2024
        message = "Test value is None."
        self.assertIsNotNone(firstValue, message)

    def test_none_value(self):
        secondValue = None
        message = "Test value is not None"
        self.assertIsNone(secondValue, message)

if __name__ == '__main__':
    unittest.main()
