# 1. Напишите программу, которая принимает на вход число N и выдает последовательность из N членов.
# Пример:
# Для N = 5: 1, -3, 9, -27, 81

# from tokenize import Number


# numberN = int(input('Введите число N: '))
# result = []
# for i in range(numberN):
#     result.append((-3)**i)
# print(result)


# numberN = int(input('Введите число N: '))
# for i in range(numberN):
#     print(pow(-3,i), end=", ")



# 2. Задачи на словари и списки

# n = int(input('Введите число: '))

# dict = {}

# for i in range(1, n+1):
#     dict[i] = 3*i+1

# print(dict)
# dict[4] = "Мы изменили тебя"
# print(dict)
# print(dict.get(8))


# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа определять количество вхождений одной строки в другой.

# 1 вариант:
string = "fghgjwenlklgkhlfkkwenjfgkjfhjhlgklf;df;kwen"
subString = "wen"
# print(string.count(subString))


# 2 вариант:
# total = 0
# for i in range(len(string)-len(subString)+1):
#         count = 0
#         if string[i] == subString[0]:
#             for j in range(len(subString)):
#                 if string[i+j] == subString[j]:
#                     count += 1
#             if count == len(subString):
#                 total += 1
# print (f"Строка '{subString}' входит в строку '{string}' - {total} раз(a)")


# 3 вариант:
counter = 0
for i in range(len(string)):
    if string[i:i+len(subString)] == subString:
        counter += 1
print(f'Количество вхождений - {counter}')