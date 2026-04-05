
def process_numbers(numbers):
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0
    return total, average

def process_string(text):
    length = len(text)
    upper_text = text.upper()
    return length, upper_text

# НОВОЕ: функция для задания 4
def count_words(text):
    """Считает количество слов"""
    return len(text.split())
# ПЗ6 тест CI
