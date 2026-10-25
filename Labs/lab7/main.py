from functions import sum_digits, average, normalize_text, select_numbers


def main():
    number = int(input("Введите целое число: "))
    print("Сумма цифр:", sum_digits(number))
    text_numbers = input("Введите целые числа через пробел: ")
    numbers = []

    for part in text_numbers.split():
        numbers.append(int(part))
    result = average(numbers)

    if result is None:
        print("Среднее: Нет данных")
    else:
        print("Среднее:", f"{result:.2f}")
    text = input("Введите текст: ")
    print("Нормализованный текст:", normalize_text(text))

    threshold = int(input("Введите неотрицательный порог: "))
    selected = select_numbers(numbers, threshold)
    print("Выбранные числа:", selected)


if __name__ == "__main__":
    main()