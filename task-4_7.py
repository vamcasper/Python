# Задание 7

from math import factorial


def fact(n: int):
    for el in range(1, n + 1):
        yield factorial(el)


n = int(input('Пожалуйста, введите количество вычисленных факториалов: '))
for el in fact(n):
    print(el)
