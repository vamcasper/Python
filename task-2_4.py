# Задание 4

my_str = input("Введите строку: ")
my_word = my_str.split(' ')
for i, el in enumerate(my_word, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}. {el}")
