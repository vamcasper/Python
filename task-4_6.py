# Задание 6

from itertools import count
from itertools import cycle


def my_count_func(start_number, stop_number):
    for el in count(start_number):
        if el > stop_number:
            break
        else:
            print(el)


def my_cycle_func(my_list, iteration):
    i = 0
    iter = cycle(my_list)
    while i < iteration:
        print(next(iter))
        i += 1


my_count_func(start_number=int(input("Введите начальное число для генерации: ")),
              stop_number=int(input("Введите число для окончания генерации: ")))
my_cycle_func(my_list=[1, 2], iteration=int(input("Количество элементов повторения: ")))
