import unittest


class MyTestCase(unittest.TestCase):
    def test_average_exception(self):
        with self.assertRaises(ValueError):
            average(-90, 89, 78)
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
