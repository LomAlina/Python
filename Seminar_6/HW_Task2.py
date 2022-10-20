# Задача: предложить улучшения кода для уже решённых задач.
# С помощью использования lambda, filter, map, zip, enumerate, list comprehension.

# Условие задачи (Семинар 4, Задача 3):
# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

from random import randint

listStr = " ".join(list(map(str, [randint(0,9) for i in range(20)])))
print(f'Задана последовательность цифр {listStr}')
finalStr = list(filter(lambda x: listStr.count(x)==1, listStr))
finalStr = list(map(int, finalStr)) 
print(f'Cписок неповторяющихся элементов исходной последовательности {finalStr}')