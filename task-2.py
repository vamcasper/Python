# Задание 2
name = input('Введите своё имя: ')
seconds = int(input(f'{name}, пожалуйста, введите время в секундах: '))
minutes = seconds // 60
hours = minutes // 60
print(f'Время в формате чч:мм:сс - {hours:02d}:{minutes%60:02d}:{seconds%60:02d}')
