# Задание 5

from functools import reduce


def my_func(el_p, el):
    return el_p * el


print(f'Список четных значений: {[el for el in range(100, 1001) if el % 2 == 0]}')
print(f'Результат перемножения всех четных чисел: {reduce(my_func, [el for el in range(100, 1001) if el % 2 == 0])}')
