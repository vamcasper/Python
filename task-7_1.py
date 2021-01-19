# Задание 1

class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matr = [[1, 2, 2],
                [4, 4, 8],
                [12, 20, 20]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matr[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))


    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))



my_matrix = Matrix([[6, 10, 12],
                    [6, 7, 3],
                    [11, 60, 13]],
                   [[42, 10, 4],
                    [6, 10, 92],
                    [20, 6, 91]])

print(my_matrix.__add__())
