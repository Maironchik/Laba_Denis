subject1_name = input("Введите название первого предмета: ")
subject1_count = int(input("Количество занятий в неделю: "))
subject1_duration = int(input("Продолжительность одного занятия (мин): "))

subject2_name = input("Введите название второго предмета: ")
subject2_count = int(input("Количество занятий в неделю: "))
subject2_duration = int(input("Продолжительность одного занятия (мин): "))

available_hours = float(input("Доступное время на неделю (в часах): "))

time_subject1_min = subject1_count * subject1_duration
time_subject2_min = subject2_count * subject2_duration

total_min = time_subject1_min + time_subject2_min
total_hours = total_min / 60

free_hours = available_hours - total_hours
total_4_weeks_hours = total_hours * 4

print(f"\nВремя на {subject1_name}: {time_subject1_min} мин.")
print(f"Время на {subject2_name}: {time_subject2_min} мин.")
print(f"Общая нагрузка: {total_min} мин. ({total_hours:.2f} ч.)")
print(f"Остаток свободного времени: {free_hours:.2f} ч.")
print(f"Нагрузка за 4 недели: {total_4_weeks_hours:.2f} ч.")