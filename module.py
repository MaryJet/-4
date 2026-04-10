def process_numbers(numbers):
    """Обработка списка чисел: сумма и среднее"""
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0
    return total, average


def process_numbers_extended(numbers):
    """Расширенная обработка: сумма, среднее и произведение"""

    def multi(nums):
        itog = 1
        for num in nums:
            itog *= num
        return itog

    total = sum(numbers)
    multiplication = multi(numbers)
    average = total / len(numbers) if numbers else 0
    return total, average, multiplication


def process_string(text):
    """Обработка строки: длина и верхний регистр"""
    length = len(text)
    upper_text = text.upper()
    return length, upper_text


def process_string_extended(text):
    """Расширенная обработка: длина, верхний и нижний регистр"""
    length = len(text)
    upper_text = text.upper()
    lower_text = text.lower()
    return length, upper_text, lower_text


def count_words(text):
    """Считает количество слов в строке"""
    return len(text.split())


def main():
    """Основная функция с пользовательским вводом"""
    nums = input("Введите числа через пробел: ")
    nums_list = list(map(int, nums.split()))

    total, avg = process_numbers(nums_list)
    print("Сумма:", total)
    print("Среднее:", avg)

    text = input("Введите строку: ")
    length, upper = process_string(text)
    print("Длина строки:", length)
    print("Верхний регистр:", upper)

    words = count_words(text)
    print("Количество слов:", words)


if __name__ == "__main__":
    main()