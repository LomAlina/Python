# 3. Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

# Вариант 1:

from random import randint
from typing import final

newList = {}
finalStr = ''
listStr = "".join(list(map(str, [randint(0,9) for i in range(40)])))
print(f'Задана последовательность цифр {listStr}')

for c in listStr:
    if newList.get(c):
        newList[c] = newList.get(c) + 1
    else:
        newList[c] = 1

print(newList)

for k,v in newList.items():
    if v == 1:
        finalStr += str(k) + " "

print(f'Уникальные цифры {finalStr}') if finalStr else print('Уникальных позиций нет')


# Вариант 2:

# import random
# list_0 = [random.randint(0,50) for i in range (15)]
# print('Исходный список ', list_0)
# new_list =[]
# [new_list.append(i) for i in list_0 if i not in new_list ]
# print('Список без повторяющихся элементов ', new_list)