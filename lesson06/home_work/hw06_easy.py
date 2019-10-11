# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


import math


def isflatpoint(var):
    if not isinstance(var, (tuple, list,)):
        return False
    if len(var) != 2:
        return False
    if not all(map(lambda x: isinstance(x, (int, float,)), var)):
        return False
    return True


class Triangle:
    """
    Треугольник задаётся координатами трёх его вершин -
    a, b и c, представленными в видё кортежей (x, y)
    """

    def __init__(self, a, b, c):
        if not all(map(isflatpoint, (a, b, c,))):
            raise TypeError('Точка должна быть списком или кортежем координат x и y')
        if any((a == b, a == c, b == c)):
            raise ValueError('Минимум две из заданных точек совпадают')
        self._a, self._b, self._c = a, b, c
        if any(self.height(base) == 0 for base in ('ab', 'ac', 'bc')):
            raise ValueError('Заданные точки образуют треугольник, вырожденный в линию')

    @property
    def _sides(self):
        len_ab = math.sqrt((self._b[0] - self._a[0])**2 + (self._b[1] - self._a[1])**2)
        len_ac = math.sqrt((self._c[0] - self._a[0])**2 + (self._c[1] - self._a[1])**2)
        len_bc = math.sqrt((self._c[0] - self._b[0])**2 + (self._c[1] - self._b[1])**2)
        return len_ab, len_ac, len_bc

    @property
    def perimeter(self):
        return sum(self._sides)

    @property
    def square(self):
        hp = self.perimeter / 2
        len_ab, len_ac, len_bc = self._sides
        return math.sqrt(hp * (hp - len_ab) * (hp - len_bc) * (hp - len_ac))

    def height(self, base):
        """
        строковый параметр, обозначающий сторону треугольника,
        к которой проведена высота - ab, ac или bc
        """
        bases = dict(list(zip(['ab', 'ac', 'bc'], self._sides)))
        if not base in bases:
            raise ValueError('Неверно задан параметр функции height - {}'.format(base))
        return self.square * 2 / bases[base]

    def __str__(self):
        return 'Треугольник a {} - b {} - c {}'.format(self._a, self._b, self._c)


if __name__ == '__main__':
    triag1 = Triangle((0, 10), (0, 0), (10, 0))
    print(triag1)
    print('Периметр =', triag1.perimeter)
    print('Площадь =', triag1.square)
    print('Высота из вершины c к стороне ab =', triag1.height('ab'))
    print('Высота из вершины b к стороне ac =', triag1.height('ac'))
    print('Высота из вершины a к стороне bc =', triag1.height('bc'))
    # print('Длины сторон ab, ac, bc =', triag1._sides)


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class IsoscelesTrapezoid:
    """
    Трапеция задаётся координатами четырёх её вершин -
    a, b, c и d, представленными в видё кортежей (x, y)
    """
    def __init__(self, a, b, c, d):
        if not all(map(isflatpoint, (a, b, c, d,))):
            raise TypeError('Точка должна быть списком или кортежем координат x и y')
        if any(map(lambda p: p[0] == p[1], zip((a, b, c, a, b, a,), (b, c, d, c, d, d,)))):
            raise ValueError('Минимум две из заданных точек совпадают')
        self._a, self._b, self._c, self._d = a, b, c, d
