# Задание 4

rus = {'One': 'Один ', 'Two': 'Два ', 'Three': 'Три ', 'Four': 'Четыре '}
new_file = []
with open('file_4.txt', 'r', encoding='utf-8') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + i[1])
    print(new_file)

with open('file_4_new.txt', 'w', encoding='utf-8') as file_obj_2:
    file_obj_2.writelines(new_file)
