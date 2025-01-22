# Вводим четыре числа
a = int(input())
b = int(input())
c = int(input())
d = int(input())

# Изначально предполагаем, что первое число минимальное
min_value = a

# Сравниваем с другими числами и обновляем минимальное значение
if b < min_value:
    min_value = b
if c < min_value:
    min_value = c
if d < min_value:
    min_value = d

# Выводим результат
print(min_value)

# ---------Напишите программу, которая 
# ---------упорядочивает три числа от большего к меньшему.

# Считываем три числа
a = int(input())
b = int(input())
c = int(input())

# Находим максимальное, минимальное и среднее значения
maximum = max(a, b, c)
minimum = min(a, b, c)

# Находим среднее значение через сумму всех чисел минус максимум и минимум
middle = a + b + c - maximum - minimum

# Выводим числа в порядке убывания
print(maximum)
print(middle)
print(minimum)


