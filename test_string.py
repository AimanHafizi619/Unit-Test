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

class TestInstance(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(1, int)
        self.assertIsInstance("hello", str)
        self.assertIsInstance(1.0, float)

    def test_not_instance(self):
        self.assertNotIsInstance(1, str)
        self.assertNotIsInstance("hello", int)
        self.assertNotIsInstance(1.0, str)

class TestClass:
    x = 5

class TestClass_minor:
    x = 6

class TestObjectInstance(unittest.TestCase):

    def test_object_isInstance(self):
        objectName = TestClass()
        message = "Given object is an instance of TestClass."
        self.assertIsInstance(objectName, TestClass, message)

    def test_object_notIsInstance(self):
        objectName = TestClass()
        message = "Given object is not an instance of TestClass."
        self.assertNotIsInstance(objectName, TestClass_minor, message)

class TestNotAlmostEqual(unittest.TestCase):
    
    def test_count_decimalPlace(self):
        first_num = 4.4555
        second_num = 4.4566

        decimalPlace_1 = 2
        decimalPlace_2 = 3

        message1 = "first and second are almost equal."
        message2 = "first and second are almost not equal."

        self.assertAlmostEqual(first_num, second_num, decimalPlace_1, message1)
        self.assertNotAlmostEqual(first_num, second_num, decimalPlace_2, message2)

    def test_count_deltaPlace(self):
        first_num = 4.4555
        second_num = 4.4566

        delta1 = 0.002
        delta2 = 0.0001

        message1 = "first and second are almost equal."
        message2 = "first and second are almost not equal."

        self.assertAlmostEqual(first_num, second_num, None, message1, delta1)
        self.assertNotAlmostEqual(first_num, second_num, None, message2, delta2)

if __name__ == '__main__':
    unittest.main()
