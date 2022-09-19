# tests for the string_to_lower() function
import unittest


class TestStringToLower(unittest.TestCase):
    def test_string_to_lower(self):
        # testing for an exception one way
        test_data = [0, 0.0, None, [], {}, ()]
        for x in test_data:
            self.assertRaises(ValueError, string_to_lower, x)

        # testing for an exception another way
        for x in test_data:
            with self.assertRaises(ValueError):
                string_to_lower(x)

if __name__ == '__main__':
    unittest.main()