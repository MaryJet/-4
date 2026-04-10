
def process_numbers(numbers):
    def multi(numbers):
        if numbers:
            itog = 1
        else:
            itog = 0
        for i in range(len(numbers)):
            itog = itog * numbers[i]
        return itog
    total = sum(numbers)
    multiplication = multi(numbers)
    average = total / len(numbers) if numbers else 0
    return total, average, multiplication

def process_string(text):
    length = len(text)
    upper_text = text.upper()
    lower_text = text.lower()
    return length, upper_text, lower_text

def main():
    nums = input("Введите числа через пробел: ")
    nums_list = list(map(int, nums.split()))

    total, avg, multi = process_numbers(nums_list)
    print("Сумма:", total)
    print('Произведение:', multi)
    print("Среднее:", avg)


    text = input("Введите строку: ")
    length, upper, lower = process_string(text)
    print("Длина строки:", length)
    print("Верхний регистр:", upper)
    print("Нижний регистр:", lower)

if __name__ == "__main__":
    main()
