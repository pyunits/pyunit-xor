import unittest

from pyunit_xor import SimpleXOR


class MyTestCase(unittest.TestCase):
    def test_something(self):
        manager = SimpleXOR()
        tokens = manager.generate("2125-01-10 00:00:00")
        is_valid, _ = manager.validate(tokens)
        self.assertEqual(True, is_valid)

        tokens = manager.generate("1999-01-10 00:00:00")
        is_valid, _ = manager.validate(tokens)
        self.assertEqual(False, is_valid)


if __name__ == '__main__':
    unittest.main()
