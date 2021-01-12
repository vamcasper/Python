# Задание 2
def my_info(name, surname, birthday, city, email, phone):
    print(f'Имя - {name}; Фамилия -{surname}; Год рождения - {birthday};'
          f'Город проживания - {city}; Электронная почта - {email}; Телефон - {phone}')


my_info(name=input('Введите Ваше имя: '), surname=input('Введите Вашу фамилию: '),
        birthday=int(input('Введите год Вашего рожения: ')),
        city=input('Введите город проживания: '),
        email=input('Введите адрес Вашей электронной почты: '), phone=input('Введите номер телефона: '))
