# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

# Вариант 1:

from operator import eq
import random
def createDict():
    equation = {}
    degree = int(input('Введите максимальную степень многочлена: '))
    for i in range(degree, -1, -1):
        equation[i] = random.randint(-10,10)
    return equation

def createEquation(equation: dict):
    strEquation = ''
    first = True

    for k,v in equation.items():
        if first:
            first = False
            if v > 0:
                strEquation += f'{v}*x^{k}'
            elif v < 0:
                strEquation += f'- {abs(v)}*x^{k}'
        else:
            if v > 0:
                strEquation += f' + {v}*x^{k}'
            elif v < 0:
                strEquation += f' - {abs(v)}*x^{k}'

    return strEquation

def printEquation(equation: str):
    print(equation.replace('*x^1', 'x').replace('*x^0', '') + ' = 0')

print(createEquation(createDict()).replace(' + ', '+'))

equation = '1*x^9 - 10*x^7 + 7*x^6 + 8*x^5 + 3*x^4 + 6*x^3 + 7*x^2 - 7*x^1 - 5*x^0'

def parseEquation(equation: str):
    eqDict = {}
    equation = equation.replace(' + ', ' +').replace(' - ', ' -')
    equation = equation.split()
    
    for i in equation:
        element = i.split('*x^')
        eqDict[int(element[1])] = int(element[0])
        
    return eqDict

path = 'task4.txt'
with open(path, 'w', encoding='UTF-8') as data:
    data.write(equation)


# Вариант 2:

# import random

# k = int(input('Введите коэффициент: '))
# a = int(random.randint(0,100))
# b = int(random.randint(0,100))
# c = int(random.randint(0,100))

# if a != 0:
#     first = (str(a) + "x^" + str(k) + " + ")
# else:
#     first = (str())

# if b != 0:
#     second = (str(b) + "x" + " + ")
# else:
#     second = (str())

# if c != 0:
#     third = (str(c) + " = 0")
# else:
#     third = (str())

# print(f'{first}{second}{third}')