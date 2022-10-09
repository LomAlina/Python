# Задание 5.
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] (Негафибоначчи)

k = int(input('Введите число k: '))
fib_list = [0]*(k*2+1)
fib_list[k] = 0
fib_list[k+1] = 1
for i in range(k+2, len(fib_list)):
    fib_list[i] = fib_list[i-2] + fib_list[i-1]

for i in range(k, -1, -1):
    fib_list[i] = fib_list[i+2] - fib_list[i+1]
print(fib_list)