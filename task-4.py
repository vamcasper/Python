# Задание 4

while True:
    number = int(input('Введите любое целое положительное число: '))
    if number > 0:
        maximum = number%10
        number = number//10
        while number > 0:
            if number%10 > maximum:
                maximum = number%10
            number = number//10
        print(f'Максимальное число в вашей цифре равно {maximum}')
        break
    else:
        print('Ваше число отрицательно!')