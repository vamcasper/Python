# Задание 3

while True:
    number = int(input('Введите любое число n от 0 до 9 включительно: '))
    if number >= 0 and number <= 9:
        print(f'Сумма чисел n+nn+nnn равно {number + number * 11 + number * 111}')
    else:
        print('Ваше число не входит в указанный диапазон!')
