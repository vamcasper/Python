# Задание № 3

with open('file_3.txt', 'r', encoding='utf-8') as my_file:
    salary = []
    poor = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           poor.append(i[0])
        salary.append(i[1])
print(f'Оклад меньше 20,0 тыс. руб. у {poor} \nСредний оклад {sum(map(int, salary)) / len(salary)}')
