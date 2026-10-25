from functions import average, normalize_text, select_numbers, sum_digits


# Проверки суммы цифр
assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert sum_digits(999) == 27
assert sum_digits(-12) == 3

# Проверки среднего значения
assert average([]) is None
assert average([2, 4, 6]) == 4
assert abs(average([1, 2]) - 1.5) < 1e-9
assert average([-2, 0, 2]) == 0

# Проверки нормализации текста
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""
assert normalize_text("Python") == "python"
assert normalize_text("  Два\tслова\nвместе ") == "два слова вместе"

# Проверки индивидуального варианта 3
numbers = [-5, 0, 2, 5]
original = numbers.copy()

assert select_numbers(numbers, 2) == [-5, 5]
assert numbers == original

# Пустой список
assert select_numbers([], 2) == []

# Граничные значения: модуль равен порогу — не подходит
assert select_numbers([-2, 2], 2) == []

# Значения рядом с границей
assert select_numbers([-3, -2, 2, 3], 2) == [-3, 3]

# Повторы подходящих чисел сохраняются
assert select_numbers([5, 5, -5, 2], 2) == [5, 5, -5]

# Если подходящих чисел нет
assert select_numbers([0, 1, -2, 2], 2) == []

# Проверка, что исходный список не изменился
numbers = [-8, 2, 6, 6]
original = numbers.copy()
select_numbers(numbers, 2)
assert numbers == original

print("Все проверки пройдены")