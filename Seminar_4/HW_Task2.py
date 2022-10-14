# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# Вариант 1:

import numbers

numbers = int(input("Введите число: "))

devList = []
dev = 2
while numbers > 2:
    if numbers % dev != 0:
        dev += 1
    else:
        numbers //= dev
        devList.append(dev)
        print(devList)

print(set(devList))


# Вариант 2:

# def check_number_simple(n: int):
#     i = 2
#     while n % i != 0 or i == n - 1:
#         i += 1
#     if i == n:
#         return n

# def fill_simple_list(n: int) -> list:
#     simple_list = [1]
#     for i in range(2, n+1):
#         if n % i == 0:
#             if check_number_simple(i) != None:
#                 simple_list.append(check_number_simple(i))
#             else:
#                 continue
#     return simple_list

# N = int(input('Введите число N: '))
# simple_list = fill_simple_list(N)
# print(simple_list)