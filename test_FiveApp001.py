import unittest
from FiveApp001 import get_number

class TestFiveApp001(unittest.TestCase):
    def test_get_number(self):
        self.assertEqual(get_number(), 5)

if __name__ == '__main__':
    unittest.main()
