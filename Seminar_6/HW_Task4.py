path = 'newtask1.txt'

with open(path, 'r', encoding='UTF-8') as data:
    equation1 = data.readline()

# equation1 = equation1.replace(' = 0', '').replace(' + ', ' ').replace(' - ', ' -').split(' ')
print(equation1)

def parseEquation(equation1: str):
    eqDict = {}
    equation1 = equation1.replace(' = 0', '').replace(' + ', ' ').replace(' - ', ' -').split(' ')
    
    for i in equation1:
        element = i.split('*x^')
        eqDict[int(element[1])] = int(element[0])
        
    return eqDict

print(parseEquation)





# from operator import eq
# import random
# def createDict():
#     equation = {}
#     degree = int(input('Введите максимальную степень многочлена: '))
#     for i in range(degree, -1, -1):
#         equation[i] = random.randint(-10,10)
#     return equation

# def createEquation(equation1: dict):
#     strEquation = ''
#     first = True

#     for k,v in equation.items():
#         if first:
#             first = False
#             if v > 0:
#                 strEquation += f'{v}*x^{k}'
#             elif v < 0:
#                 strEquation += f'- {abs(v)}*x^{k}'
#         else:
#             if v > 0:
#                 strEquation += f' + {v}*x^{k}'
#             elif v < 0:
#                 strEquation += f' - {abs(v)}*x^{k}'

#     return strEquation

# def printEquation(equation: str):
#     print(equation.replace('*x^1', 'x').replace('*x^0', '') + ' = 0')

# def parseEquation(equation: str):
#     eqDict = {}
#     equation.replace(' + ', ' +').replace(' - ', ' -')
#     equation = equation.split()
    
#     for i in equation:
#         element = i.split('*x^')
#         eqDict[int(element[1])] = int(element[0])
        
#     return eqDict

# def summEquation(equation1: dict, equation2: dict):
#     finalEquation = {}

#     for i in range(max(len(equation1), len(equation2)), -1, -1):
#         if equation1.get(i) or equation2.get(i):
#             finalEquation[i] = (equation1.get(i) if equation1.get(i) else 0) + (equation2.get(i) if equation2.get(i) else 0)
#     return finalEquation

# equation1 = createDict()
# equation2 = createDict()

# finalEquation = summEquation(equation1, equation2)

# printEquation(createEquation(equation1))
# printEquation(createEquation(equation2))
# printEquation(createEquation(finalEquation))