# Задание 3.
# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов. 
# Если число целое, то его дробная часть не считается за 0 и оно (число) в сравнении не участвует.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list_0 = [1.1, 1.2, 3.1, 5.1, 10.01]
def dif(list_0):
    dif_max_min =[]
    for i in range(len(list_0)):
        dif_max_min.append(list_0[i]%1)
    return max(dif_max_min) - min(dif_max_min)
print(list_0, ' => ', round(dif(list_0),2))