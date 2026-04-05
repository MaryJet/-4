
def process_numbers(numbers):
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0
    return total, average

def process_string(text):
    length = len(text)
    upper_text = text.upper()
    return length, upper_text

def main():
    nums = input("Введите числа через пробел: ")
    nums_list = list(map(int, nums.split()))

    total, avg = process_numbers(nums_list)
    print("Сумма:", total)
    print("Среднее:", avg)

    text = input("Введите строку: ")
    length, upper = process_string(text)
    print("Длина строки:", length)
    print("Верхний регистр:", upper)

if __name__ == "__main__":
    main()
