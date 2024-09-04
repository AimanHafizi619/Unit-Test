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

if __name__ == '__main__':
    unittest.main()
    