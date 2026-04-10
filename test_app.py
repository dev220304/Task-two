import unittest
from buggy import add   # initially testing buggy file

class TestAdd(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()