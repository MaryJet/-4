
import unittest
from module import process_numbers, process_string, count_words

class TestModule(unittest.TestCase):
    def test_process_numbers_sum(self):
        total, avg = process_numbers([1, 2, 3])
        self.assertEqual(total, 6)
        self.assertAlmostEqual(avg, 2.0)

    def test_process_numbers_empty(self):
        total, avg = process_numbers([])
        self.assertEqual(total, 0)
        self.assertEqual(avg, 0)

    def test_process_numbers_negative(self):
        total, avg = process_numbers([-1, -2, -3])
        self.assertEqual(total, -6)
        self.assertAlmostEqual(avg, -2.0)

    def test_process_string(self):
        length, upper = process_string('hello')
        self.assertEqual(length, 5)
        self.assertEqual(upper, 'HELLO')

    def test_count_words(self):
        count = count_words('hello world test')
        self.assertEqual(count, 3)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
