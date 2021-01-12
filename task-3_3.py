# Задание 3
def my_func(arg_1, arg_2, arg_3):
    if arg_1 >= arg_3 and arg_2 >= arg_3:
        return arg_1 + arg_2
    elif arg_1 >= arg_2 and arg_3 >= arg_2:
        return arg_1 + arg_3
    else:
        return arg_2 + arg_3


print(f'Сумма двух наибольших аргументов равняется {my_func(int(input("Введите первый аргмент: ")), int(input("Введите второй аргумент: ")), int(input("Введите третий аргмент: ")))}')
