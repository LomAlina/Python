# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# Примеры:
# 5, 25 -> да
# 4, 16 -> да
# 25, 5 -> да
# 8,9 -> нет

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# if b == a*a or a == b*b:
#     print("да")
# else:
#     print("Нет")



# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#     Примеры:
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

# array = []
# for i in range(5):
#     array.append(int(input('Введите число ')))
# print(array)

# max = array[0]


# for i in range(len(array)):
#     if max <= array[i]:
#         max = array[i]
# print(max)



# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
#     Примеры:
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# N = int(input('N равно: '))
# array = []
# for i in range(-N, N+1):
#     array.append(i)
# print(array)



# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
#     Примеры:
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3
# 0,5 -> 5
# 45,098 -> 0


from math import floor


a = float(input('Введите дробное число: '))
a = a*10
result = floor(a%10)
# print(a)
print(result)