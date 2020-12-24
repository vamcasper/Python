# Задание 4
# Вариант 1:
def my_func(x, y):
    return 1 / x ** abs(y)


print(f'Результат возведения числа x в степень y равняется {my_func(int(input("Введите положительное число x: ")), int(input("Введите отрицательное число y: ")))}')

# Вариант 2:


def my_func2(x2, y2):
    result = x2
    for el in range(abs(y2) - 1):
        result *= x2
    return 1 / result

x2 = int(input('Введите положительное число x: '))
y2 = int(input('Введите отрицательное число y: '))
print(f'Результат возведения числа x в степень у равняется {my_func2(x2, y2)}')
