# Задание 3

list = ('зима', 'весна', 'лето', 'осень')
# Вариант 1
number = int(input('Введите месяц в виде цифры от 1 до 12 включительно: '))
if number == 1 or number == 2 or number == 12:
    print('Вариант 1: ', list[0])
elif number == 3 or number == 4 or number == 5:
    print('Вариант 1: ', list[1])
elif number == 6 or number == 7 or number == 8:
    print('Вариант 1: ', list[2])
elif number == 9 or number == 10 or number == 11:
    print('Вариант 1: ', list[3])
else:
    print('Ошибка. Ваше число меньше нуля или больше 12.')

# Вариант 2
seasons = {'зима': (1, 2, 12),
           'весна': (3, 4, 5),
           'лето': (6, 7, 8),
           'осень': (9, 10, 11)}
for key in seasons.keys():
    if number in seasons[key]:
        print('Вариант 2: ', key)
