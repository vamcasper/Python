# Задание 1

from sys import argv

file_name, worked_hour, rate, benefit = argv
print('Имя скрипта: ', file_name)
print('Отбработанное время: ', worked_hour)
print('Ставка: ', rate)
print('Премия: ', benefit)

salary = (int(worked_hour) * int(rate)) + int(benefit)
print(f'Ваша заработная плата составит {salary}')
