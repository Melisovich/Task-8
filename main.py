import random

# Линейные алгоритмы


# 1. Перевод граммов в килограммы
grams = int(input("Введите значение в граммах: "))
kilograms = grams / 1000
print(f"Вес в килограммах: {kilograms} кг")

# 2. Поменять значения переменных местами
x = 10
y = 55
print("Значения переменных до замены:")
print(f"x = {x}, y = {y}")
x, y = y, x
print("Значения переменных после замены:")
print(f"x = {x}, y = {y}")

# 3. Найти количество полных километров
distance_meters = float(input("Введите расстояние в метрах: "))
kilometers = distance_meters // 1000
print(f"Количество полных километров: {kilometers} км")

# 4. Вывести число, обратное по порядку цифр
number = int(input("Введите целое число: "))
reversed_number = int(str(number)[::-1])
print(f"Обратное число: {reversed_number}")

# 5. Получить и преобразовать текущую системную дату
from datetime import date
today = date.today()
formatted_date = today.strftime("%d.%m.%Y")
print(f"Текущая дата в формате день.месяц.год: {formatted_date}")











# Логические выражения


# 1. Условие, когда хотя бы одно из чисел x, y и z больше 80
x = 75
y = 90
z = 60
condition1 = x > 80 or y > 80 or z > 80
print(f"Условие, когда хотя бы одно из чисел больше 80: {condition1}")

# 2. Условие, когда оба числа a и b одновременно положительны или отрицательны
a = -10
b = 5
condition2 = (a > 0 and b > 0) or (a < 0 and b < 0)
print(f"Условие, когда оба числа одновременно положительны или отрицательны: {condition2}")

# 3. Нахождение наименьшего из трех чисел
numbers = [130, 25, 70]
min_number = min(numbers)
print(f"Наименьшее число: {min_number}")




# Циклы


# 1. Подсчет количества символов в строке с использованием циклов for и while
string = 'Python - это Питон!'

# С использованием цикла for
count_for = 0
for char in string:
    count_for += 1
print(f"Количество символов (for): {count_for}")

# С использованием цикла while
count_while = 0
index = 0
while index < len(string):
    count_while += 1
    index += 1
print(f"Количество символов (while): {count_while}")

# 2. Нахождение суммы всех элементов списка
my_list = [1, '2', 3, 4, '5']
sum_list = 0
for item in my_list:
    if isinstance(item, int):
        sum_list += item
    elif isinstance(item, str) and item.isdigit():
        sum_list += int(item)
print(f"Сумма элементов списка: {sum_list}")

# 3. Проверка наличия символов в строке
string1 = 'abcde123'
string2 = 'bad_cat_23'
for char in string1:
    if char in string2:
        print(f'Символ "{char}" есть в "{string2}".')
    else:
        print(f'Символа "{char}" нет в "{string2}".')

# 4. Генерация и вывод на экран мозаичного изображения гексагональной сетки
size = 5
for i in range(2 * size - 1):
    line = ' ' * abs(size - 1 - i)
    if i < size:
        line += ' / \\ ' * (size + i)
    else:
        line += ' \\ / ' * (3 * size - 1 - i)
    print(line)

# 5. Генерация таблицы Пифагора
print("  ┌─────────────────────────────────────────────┐")
print("  │       1   2   3   4   5   6   7   8   9       │")
print("  ├─────────────────────────────────────────────┤")

for i in range(1, 10):
    print(f"{i} │", end=" ")
    for j in range(1, 10):
        result = i * j
        print(f"{result:3d}", end=" │ ")
    print()
    if i != 9:
        print("  ├─" + "───┼─" * 8 + "───┤")

print("  └─────────────────────────────────────────────┘")










# Функции


def generate_password():
    length = random.randint(8, 15)
    password = ""
    for _ in range(length):
        category = random.randint(1, 3)
        if category == 1:
            password += chr(random.randint(48, 57))
        elif category == 2:
            password += chr(random.randint(65, 90))
        else:
            password += chr(random.randint(97, 122))
    return password


for _ in range(3):
    password = generate_password()
    print(password)


