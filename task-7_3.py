# Задание 3

class Cell:
    def __init__(self, count: int):
        self._count = count

    def __add__(self, other: "Cell") -> "Cell":
        return Cell(self._count + other._count)

    def __sub__(self, other: "Cell") -> "Cell":
        if self._count > other._count:
            return Cell(self._count - other._count)

        print(f"{self._count} - {other._count}: операция невозможна")

    def __mul__(self, other: "Cell") -> "Cell":
        return Cell(self._count * other._count)

    def __truediv__(self, other: "Cell") -> "Cell":
        return Cell(self._count // other._count)

    def make_order(self, per_row: int) -> str:
        rows, tail = self._count // per_row, self._count % per_row
        return '\n'.join(['*' * per_row] * rows + (['*' * tail] if tail else []))

    def __str__(self) -> str:
        return f"Клетка состоит из {self._count} ячеек"


if __name__ == '__main__':
    c1 = Cell(12)
    print(c1)
    c2 = Cell(5)
    print(c2)

    print(f'Сложение: {c1 + c2}')
    print(f'Вычитание второй клетки из первой: {c1 - c2}')
    print(f'Вычитание первой клетки из второй: {c2 - c1}')
    print(f'Умножение: {c1 * c2}')
    print(f'Деление первой клетки на вторую: {c1 / c2}')
    print(f'Деление второй клетки на первую: {c2 / c1}')
    print((c1 * c2).make_order(9))
