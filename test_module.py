import unittest
from module import process_numbers, process_string, count_words


class TestModule(unittest.TestCase):

    def test_numbers_positive(self):
        """Тест 1: положительные числа"""
        total, avg = process_numbers([5, 10, 15])
        self.assertEqual(total, 30)
        self.assertEqual(avg, 10.0)

    def test_numbers_negative(self):
        """Тест 2: отрицательные числа"""
        total, avg = process_numbers([-5, -10])
        self.assertEqual(total, -15)
        self.assertEqual(avg, -7.5)

    def test_numbers_empty(self):
        """Тест 3: пустой список"""
        total, avg = process_numbers([])
        self.assertEqual(total, 0)
        self.assertEqual(avg, 0)

    def test_string_russian(self):
        """Тест 4: русская строка"""
        length, upper = process_string("Привет")
        self.assertEqual(length, 6)
        self.assertEqual(upper, "ПРИВЕТ")

    def test_string_english(self):
        """Тест 5: английская строка"""
        length, upper = process_string("Hello World")
        self.assertEqual(length, 11)
        self.assertEqual(upper, "HELLO WORLD")

    def test_count_words(self):
        """Тест 6: подсчёт слов"""
        count = count_words("hello world test")
        self.assertEqual(count, 3)


if __name__ == '__main__':
    unittest.main(verbosity=2)