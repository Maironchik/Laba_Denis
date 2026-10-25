def sum_digits(number):
    number = abs(number)
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total
def average(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)
def normalize_text(text):
    return " ".join(text.lower().split())
def select_numbers(numbers, threshold):
    selected = []
    for number in numbers:
        if abs(number) > threshold:
            selected.append(number)
    return selected