# Задание № 2

my_file = open('file_2.txt', 'r')
content = my_file.read()
print(f'Содержимое файла:\n {content}')
my_file = open('file_2.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
my_file = open('file_2.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Количество слов в {i + 1}-ой строке: {len(content[i].split())}')
my_file.close()
