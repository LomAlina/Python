# 5. НЕОБЯЗАТЕЛЬНО Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

# Вариант 1:
import random

num = int(input("Введите размер массива: "))

myList = []

for _ in range(num):
    myList.append(random.randint(-num, num))

print(myList)

data = open("file.txt", 'r')
coef1 = data.readline()
coef2 = data.readline()
data.close

print(coef1)
print(coef2)

print(myList[int(coef1)] * myList[int(coef2)])

# Вариант 2:
# from unittest import result
# list = [-7, 1, 2, 3, 4, 5, 7]
# x = int(input('Введите 1 позицию элемента от 0 до 6: '))
# y = int(input('Введите 2 позицию элемента от 0 до 6: '))
# z = int(input('Введите 3 позицию элемента от 0 до 6: '))

# for i in range(len(list)):
#     result = list[x -1]*list[y - 1]*list[z -1]
#     print(f'Произведение элементов {list[x -1]} * {list[y -1]} * {list[z -1]} =', result)