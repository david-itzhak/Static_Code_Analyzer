# tests for the is_even() function
import unittest


class TestIsEven(unittest.TestCase):

    def test_when_output_true(self):
        case_numbers = [2, -2, 0, 1000000000, -1000000000]
        for n in case_numbers:
            self.assertTrue(is_even(n))

    def test_when_output_false(self):
        case_numbers = [1, -1, 1000000001, -1000000001]
        for n in case_numbers:
            self.assertFalse(is_even(n))


if __name__ == '__main__':
    unittest.main()