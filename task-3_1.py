# Задание 1
def my_func(arg_1, arg_2):
    return arg_1 / arg_2


arg_1 = float(input('Введите любое число для первого аргумента: '))
while True:
    arg_2 = float(input('Введите любое число для второго аргумента: '))
    if arg_2 != 0:
        print(my_func(arg_1, arg_2))
        break
    else:
        print('Деление на ноль!')
