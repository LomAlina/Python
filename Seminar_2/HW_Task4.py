# 4. Реализуйте алгоритм перемешивания списка, без использования встроеных методов (особенно SHUFFLE, без него). 
# Можно (нужно) использовать библиотеку Random.

# Вариант 1:
import random
list = []

for _ in range(10):
    list.append(random.randint(0,50))
print('Оригинальный список: ' + str(list))

for i in range(len(list)-1):
    j = random.randint(0, len(list)-1)
    list[i], list[j] = list[j], list[i]

print('Перемешенный список: ' + str(list))


# Вариант 2:
# import random
# def mix_list(list_original):
#     list = list_original[:]
#     list_length = len(list)
#     for i in range(list_length):
#         index_aleatory = random.randint(0, list_length - 1)
#         temp = list[i]
#         list[i] = list[index_aleatory]
#         list[index_aleatory] = temp
#     return list
# list = [2, 8, 4, 3, 1, 5]
# mixed_list = mix_list(list)
# print("Исходный список: ")
# print(list)
# print("Перемешанный список: ")
# print(mixed_list)


# Вариант встроенной функции:
# import random
# list = [2, 8, 4, 3, 1, 5]
# random.shuffle(list)
# print(list)