# Написать программу сложения двух чисел

# sum = lambda a, b: a+b

# x = int(input('x= '))
# y = int(input('y= '))

# print(f'{x} + {y} = {sum (x, y)}')

# Модули:
x = 0
y = 0
def init(a, b):
    global x 
    global y
    x = a
    y = b

def do_it():
    return x + y