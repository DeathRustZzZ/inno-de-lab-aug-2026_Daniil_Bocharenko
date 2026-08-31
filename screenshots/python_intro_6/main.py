# Задание 1: Приветствие

user_input = input("Как тебя зовут?\n")
print(f"Привет, {user_input}! Приятно познакомится")

# Задание 2: Площадь прямоугольника
user_length = int(input("Введите длину прямоугольника: ").strip())
user_width = int(input("Введите ширину прямоугольника: ").strip())
print(f"Площадь прямоугольника: {user_length * user_width}")

# Задание 3: Конвертация температуры
user_temperature = float(input("Введите температуру в градусах Цельсия: ").strip())
fahrenheit = user_temperature * 9 / 5 + 32
print(f"Температура по Фаренгейту: {fahrenheit}°F")

# Задание 4: Проверка на четность
user_input = int(input("Введите число: ").strip())
if user_input % 2 == 0:
    print(f"Число {user_input} - четное")
else:
    print(f"Число {user_input} - нечетное")

# Задание 5: игра "Угадай число"
import random

secret_number = random.randint(1, 20)
attempts = 5
attempts_counter = 1
print(f"Я загадал число от 1 до 20. У тебя {attempts} попыток!")
while attempts > 0:
    user_number = int(input(f"Попытка {attempts_counter}. Введите число: ").strip())
    attempts -= 1
    attempts_counter += 1
    if user_number == secret_number:
        print("Ты угадал! Отличная работа")
        break
    elif user_number < secret_number:
        print(f"Слишком мало! Осталось попыток: {attempts}")
    else:
        print(f"Слишком много! Осталось попыток: {attempts}")

    if attempts == 0 and user_number != secret_number:
        print(f"Попытки закончились! Я загадал число {secret_number}")


# Задание 6: Калькулятор (Опциональное)
first_number = float(input("Введите первое число: ").strip())
second_number = float(input("Введите второе число: ").strip())
operator = input("Выберите оператор (+, -, *, /): ").strip()

if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    if second_number != 0:
        result = first_number / second_number
    else:
        print("Ошибка: на ноль делить нельзя!")
        result = None
else:
    print("Ошибка: неизвестный оператор!")
    result = None

if result is not None:
    print(f"Результат: {first_number} {operator} {second_number} = {result}")
