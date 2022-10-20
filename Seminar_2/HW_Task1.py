# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# НЕОБЯЗАТЕЛЬНО: Попробовать решить, не переводя числа в строку.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# num = input("Введите вещественное число: ")
# num = str(num)
# summa = 0
# for i in num:
#     if i != ".":
#         summa += int(i)
# print(f"Сумма цифр числа {num} = ", summa)


num = 0,56
num = str(num)
summa: int = 0
for i in num:
    print(i.isdigit())
    if i.isdigit():
        summa += int(i)

print(summa)
