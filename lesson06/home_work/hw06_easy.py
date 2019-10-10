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

    def __init__(self, p1, p2, p3):
        if not all(map(isflatpoint, (p1, p2, p3,))):
            raise TypeError('Точка должна быть списком или кортежем координат x и y')
        self._p_a, self._p_b, self._p_c = sorted([p1, p2, p3])

    def _sides(self):
        len_ab = math.sqrt((self._p_b[0] - self._p_a[0])**2 + (self._p_b[1] - self._p_a[1])**2)
        len_ac = math.sqrt((self._p_c[0] - self._p_a[0])**2 + (self._p_c[1] - self._p_a[1])**2)
        len_bc = math.sqrt((self._p_c[0] - self._p_b[0])**2 + (self._p_c[1] - self._p_b[1])**2)
        return len_ab, len_ac, len_bc

    def height(self):
        pass
        # len_ab, len_ac, len_bc = self._sides()
        # angle_ac = math.asin((self._p_c[1] - self._p_a[1]) / len_ac)
        # angle_bc = math.asin((self._p_c[1] - self._p_b[1]) / len_bc)
        # angle_acb = abs(angle_bc - angle_ac)

    @property
    def perimeter(self):
        return sum(self._sides())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class IsoscelesTrapezoid:
    
    def __init__(self, p1, p2, p3, p4):
        pass
