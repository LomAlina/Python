# Задача: предложить улучшения кода для уже решённых задач.
# С помощью использования lambda, filter, map, zip, enumerate, list comprehension.

# Условие задачи (Семинар 3, Задача 4):
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 => 101101
# 3 => 11
# 2 => 10

number = int(input('Введите число: '))
res = [int(i) for i in list('{0:0b}'.format(number))]
print ("Полученное двоичное число : " +  str(res))