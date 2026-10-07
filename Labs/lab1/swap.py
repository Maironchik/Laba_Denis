# Ввод названий аудиторий
first_room = input("Введите название первой аудитории: ")
second_room = input("Введите название второй аудитории: ")

# Вывод исходных значений
print(f"Исходные значения: первая — '{first_room}', вторая — '{second_room}'")

# Обмен значениями через третью переменную
temp_room = first_room
first_room = second_room
second_room = temp_room

# Вывод результата
print(f"Результат обмена: первая — '{first_room}', вторая — '{second_room}'")