# Задание № 6

subjects = {}
with open('file_6.txt', 'r', encoding='utf-8') as fh:
    for line in fh.readlines():
        data = line.replace('(', ' ').split()
        subjects[data[0][:-1]] = sum(int(i) for i in data if i.isdigit())
print(subjects)
