# 1. Запрос базовых данных заказа
order_name = input()
customer_name = input()

# 2. Первая позиция (Тетради)
item1_name = input()
item1_count = int(input())
item1_price = float(input())

# 3. Вторая позиция (Ручки)
item2_name = input()
item2_count = int(input())
item2_price = float(input())

# 4. Доставка и внесенная сумма
delivery_cost = float(input())
amount_paid = float(input())

# 5. Вычисления
item1_total = item1_count * item1_price
item2_total = item2_count * item2_price

goods_total = item1_total + item2_total
grand_total = goods_total + delivery_cost
total_items = item1_count + item2_count
change = amount_paid - grand_total

# 6. Вывод итоговой карточки заказа
print(f"Заказ: {order_name}")
print(f"Заказчик: {customer_name}")
print(f"{item1_name} | {item1_count} | {item1_price:.2f} | {item1_total:.2f}")
print(f"{item2_name} | {item2_count} | {item2_price:.2f} | {item2_total:.2f}")
print(f"Стоимость товаров: {goods_total:.2f}")
print(f"Общая стоимость с доставкой: {grand_total:.2f}")
print(f"Общее количество товаров: {total_items}")
print(f"Сдача: {change:.2f}")