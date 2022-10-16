# Задача 1. Вводим 2 числа с клавиатуры и находим НОК (наименьшее общее кратное), такое число, которое бы делилось и на то,
# и на то без остатка (минимальное и делилось)

# Вариант 1:

# a, b = 16, 20 #Ответ: 80
# number = max(a, b)
# print(number)
# while True:
#     if number%a == 0 and number%b == 0:
#         break
#     number+=1

# print(number)


# Вариант 2:

# numA = int(input('Введите первое число: '))
# numB = int(input('Введите первое число: '))

# i = 1

# while (min(numA, numB)*i)%max(numA, numB) != 0:
#     i += 1

# print(f'НОК чисел {numA} и {numB} равен {min(numA, numB)*i} (за {i} итераций)')


# Задача 2. Напишите программу вычисления арифметического выражения заданной строкой.
# Используйте операции +, -, /, *. Приоритет операций стандартный.
# Пример:
# 2+2 => 4
# 1+2*3 => 7
# 1-2*3 => -5

data = input('Введите выражение: ')
prioritet = ["*", "/", "+", "-"]

listResult = []
listResult = data.replace("+", " + ").replace("-",
                                              " - ").replace("*", " * ").replace("/", " / ")

listResult = listResult.split()

while len(listResult) > 1:
    if prioritet[0] in listResult or prioritet[1] in listResult:
        for i in range(1, len(listResult)-1):
            if listResult[i] == prioritet[0]:
                listResult[i-1] = int(listResult[i-1])*int(listResult[i+1])
                break

            elif listResult[i] == prioritet[1]:
                listResult[i-1] = int(listResult[i-1])/int(listResult[i+1])
                break
    else:
        for i in range(1, len(listResult)-1):

            if listResult[i] == prioritet[2]:
                listResult[i-1] = int(listResult[i-1])+int(listResult[i+1])
                break
            elif listResult[i] == prioritet[3]:
                listResult[i-1] = int(listResult[i-1])-int(listResult[i+1])
                break
    listResult.pop(i)
    listResult.pop(i)

print(f'{data} = {listResult[0]}')

# https://github.com/STONE17th/ExampleString

