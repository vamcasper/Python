# Задание 2

list = list(input('Введите элементы списка: '))
print('Исходный список', list)
index = 0
for element in range(int(len(list) / 2)):
    list[index], list[index + 1] = list[index + 1], list[index]
    index += 2
print('Результат:', list)
