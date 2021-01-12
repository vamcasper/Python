# Задание 2

initial_list = [300, 2, 12, 44, 1, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for el in initial_list if el > initial_list[initial_list.index(el) - 1]]
print(new_list)
