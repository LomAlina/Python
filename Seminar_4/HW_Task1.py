# 1. Вычислить число ПИ c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

# Вариант 1:

import math


d = float(input('Введите шаблон для округления: '))

def digit_after_dot_counter(num:float):
    count = 0
    div = 1
    while True:
        if not(num*div == int(num*div)):
            count += 1
            div *= 10
        else: break
    return count

print(round(math.pi, digit_after_dot_counter(d)))


# Вариант 2:

# from math import pi

# d =  int(input("Введите число для заданной точности числа Пи:\n"))
# print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')
