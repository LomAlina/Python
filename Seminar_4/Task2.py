# Считайте из файла уравление Ax(в квадрате) + Bx + С = 0 и найдите его корни с помощью 
# математических формул нахождения корней квадратного уравнения.

import math

path = r'text2.txt'
# pathWrite = r'solve.txt'

with open(path, 'r', encoding='UTF-8') as data:
    file = data.readline()

data_file = file.replace(' = 0', '').replace(' + ', ' ').replace(' - ', ' -').replace('*x**2', '').replace('*x', '').split()

a = int(data_file[0])
b = int(data_file[1])
c = int(data_file[2])

discr = b**2 - 4*a*c

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    result = f'X1 = {x1}, X2 = {x2}'
elif discr == 0:
    x = -b / (2 * a)
else:
    result = 'Корней нет'