# Задание 6
''' Начало
def int_func(word):
    return word.title()


word = input('Введите слово строчными буквами: ')
print(f'Ваше слово с заглавной начальной буквой: {int_func(word)}')
'''

''' # Решение 1
def int_func(word):
    separate_word = word.split(' ')
    total = []
    for el in separate_word:
        string_element = str(el)
        first_letter = string_element[:1].upper()
        word = first_letter + string_element[1:]
        total.append(word)
    return total


word = input('Введите фразу: ')
print(f'Ответ: {int_func(word)}')
'''

# Решение 2


def int_func(*args):
    word = input("Введите слова: ")
    print(f'Результат: {word.title()}')
    return


int_func()
