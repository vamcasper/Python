# Задание 4

initial_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_list = [el for el in initial_list if initial_list.count(el) < 2]
print(my_list)
