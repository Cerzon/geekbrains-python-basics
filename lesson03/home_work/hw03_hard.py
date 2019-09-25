__author__ = 'Ткаченко Кирилл Павлович'


# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

import re

class MyFraction:
    """
    constructor: MyFraction(string) or MyFraction(int, int, int)
    | string - literal representation of the fraction, i.e. '1 1/2', '-3 5/6'
    | int, int, int - integer part (0 if absent), dividend (0 if the fraction
    + --------------- part is absent), divider ( > 0! use 1 for default)
    supports add, sub, mul, truediv, comparison
    """
    def __init__(self, *args):
        self.negative = False
        self.entier = 0
        self.dividend = 0
        self.divider = 1
        if isinstance(args[0], str):
            match = re.match(
                r'^(?P<entier>-?\d+\b)? ?((?P<dividend>(?(entier)|-?)\d+)/(?P<divider>\d+))?$',
                args[0])
            if match is None:
                raise ValueError('Wrong fraction format. "{}" does not match to "[-][<int:entier>] [<int:dividend>/<int:divider>]"'.format(args[0]))
            if match.group('entier'):
                self.entier = int(match.group('entier'))
            if match.group('dividend'):
                self.dividend = int(match.group('dividend'))
                self.divider = int(match.group('divider'))
        elif len(args) == 3 and not False in (isinstance(x, int) for x in args):
            self.entier, self.dividend, self.divider = args
            if self.divider < 0:
                raise ValueError('Wrong fraction format. Divider must be positive')
        else:
            return None
        if self.divider == 0:
            raise ValueError('Divider can not be zero')
        if self.entier < 0:
            self.negative = True
            self.entier *= -1
        if self.dividend < 0:
            self.negative = True
            self.dividend *= -1
        self.simplify()

    def simplify(self):
        self.entier += self.dividend // self.divider
        self.dividend = self.dividend % self.divider
        for i in range(1, self.dividend // 2 + 1):
            if not self.dividend % i and not self.divider % (self.dividend // i):
                self.divider //= self.dividend // i
                self.dividend = i
                break
        if self.dividend == 0:
            self.divider = 1

    def complicate(self):
        self.dividend += self.entier * self.divider
        self.entier = 0

    def __str__(self):
        str_output = ''
        if self.entier:
            str_output = str(self.entier * (-1 if self.negative else 1))
        if self.dividend:
            if len(str_output):
                str_output += ' '
            else:
                str_output = '-' if self.negative else ''
            str_output += '{0}/{1}'.format(self.dividend, self.divider)
        return str_output

    def __add__(self, other):
        if not isinstance(other, MyFraction):
            if isinstance(other, int):
                return MyFraction(self.entier * (-1 if self.negative else 1) + other,
                    self.dividend, self.divider)
            else:
                return NotImplemented
        self.complicate()
        other.complicate()
        res_dividend = self.dividend * (-1 if self.negative else 1) * other.divider + other.dividend * (-1 if other.negative else 1) * self.divider
        self.simplify()
        other.simplify()
        return MyFraction(0, res_dividend, self.divider * other.divider)

    def __sub__(self, other):
        if not isinstance(other, MyFraction):
            if isinstance(other, int):
                return MyFraction(self.entier * (-1 if self.negative else 1) - other,
                    self.dividend, self.divider)
            else:
                return NotImplemented
        self.complicate()
        other.complicate()
        res_dividend = self.dividend * (-1 if self.negative else 1) * other.divider - other.dividend * (-1 if other.negative else 1) * self.divider
        self.simplify()
        other.simplify()
        return MyFraction(0, res_dividend, self.divider * other.divider)

    def __mul__(self, other):
        if not isinstance(other, MyFraction):
            if isinstance(other, int):
                other = MyFraction(other, 0, 1)
            else:
                return NotImplemented
        self.complicate()
        other.complicate()
        res_dividend = self.dividend * (-1 if self.negative else 1) * other.dividend * (-1 if other.negative else 1)
        self.simplify()
        other.simplify()
        return MyFraction(0, res_dividend, self.divider * other.divider)

    def __truediv__(self, other):
        if not isinstance(other, MyFraction):
            if isinstance(other, int):
                other = MyFraction(other, 0, 1)
            else:
                return NotImplemented
        self.complicate()
        other.complicate()
        res_dividend = self.dividend * (-1 if self.negative else 1) * other.divider * (-1 if other.negative else 1)
        res_divider = self.divider * other.dividend
        self.simplify()
        other.simplify()
        return MyFraction(0, res_dividend, res_divider)

    def __lt__(self, other):
        if not isinstance(other, MyFraction):
            if isinstance(other, int):
                other = MyFraction(other, 0, 1)
            else:
                return NotImplemented
        self.complicate()
        other.complicate()
        result = self.dividend * (-1 if self.negative else 1) * other.divider < other.dividend * (-1 if other.negative else 1) * self.divider
        self.simplify()
        other.simplify()
        return result

    def __le__(self, other):
        if not isinstance(other, MyFraction):
            if isinstance(other, int):
                other = MyFraction(other, 0, 1)
            else:
                return NotImplemented
        self.complicate()
        other.complicate()
        result = self.dividend * (-1 if self.negative else 1) * other.divider <= other.dividend * (-1 if other.negative else 1) * self.divider
        self.simplify()
        other.simplify()
        return result

    def __gt__(self, other):
        if not isinstance(other, MyFraction):
            if isinstance(other, int):
                other = MyFraction(other, 0, 1)
            else:
                return NotImplemented
        self.complicate()
        other.complicate()
        result = self.dividend * (-1 if self.negative else 1) * other.divider > other.dividend * (-1 if other.negative else 1) * self.divider
        self.simplify()
        other.simplify()
        return result

    def __ge__(self, other):
        if not isinstance(other, MyFraction):
            if isinstance(other, int):
                other = MyFraction(other, 0, 1)
            else:
                return NotImplemented
        self.complicate()
        other.complicate()
        result = self.dividend * (-1 if self.negative else 1) * other.divider >= other.dividend * (-1 if other.negative else 1) * self.divider
        self.simplify()
        other.simplify()
        return result

    def __eq__(self, other):
        if not isinstance(other, MyFraction):
            if isinstance(other, int):
                other = MyFraction(other, 0, 1)
            else:
                return NotImplemented
        self.complicate()
        other.complicate()
        result = self.dividend * (-1 if self.negative else 1) * other.divider == other.dividend * (-1 if other.negative else 1) * self.divider
        self.simplify()
        other.simplify()
        return result

    def __ne__(self, other):
        if not isinstance(other, MyFraction):
            if isinstance(other, int):
                other = MyFraction(other, 0, 1)
            else:
                return NotImplemented
        self.complicate()
        other.complicate()
        result = self.dividend * (-1 if self.negative else 1) * other.divider != other.dividend * (-1 if other.negative else 1) * self.divider
        self.simplify()
        other.simplify()
        return result


if __name__ == '__main__':
    print('*' * 70)
    print('Работаем с простыми дробями')
    str_input = input('Введите операцию с двумя дробными числами: ').strip()
    if str_input.find(' + ') > 0:
        first, second = (x.strip() for x in str_input.split(' + '))
        print(str_input, '=', MyFraction(first) + MyFraction(second))
    if str_input.find(' - ') > 0:
        first, second = (x.strip() for x in str_input.split(' - '))
        print(str_input, '=', MyFraction(first) - MyFraction(second))
    if str_input.find(' * ') > 0:
        first, second = (x.strip() for x in str_input.split(' * '))
        print(str_input, '=', MyFraction(first) * MyFraction(second))
    if str_input.find(' / ') > 0:
        first, second = (x.strip() for x in str_input.split(' / '))
        print(str_input, '=', MyFraction(first) / MyFraction(second))
    if str_input.find(' > ') > 0:
        first, second = (x.strip() for x in str_input.split(' > '))
        print(str_input, '=', MyFraction(first) > MyFraction(second))
    if str_input.find(' >= ') > 0:
        first, second = (x.strip() for x in str_input.split(' >= '))
        print(str_input, '=', MyFraction(first) >= MyFraction(second))
    if str_input.find(' < ') > 0:
        first, second = (x.strip() for x in str_input.split(' < '))
        print(str_input, '=', MyFraction(first) < MyFraction(second))
    if str_input.find(' <= ') > 0:
        first, second = (x.strip() for x in str_input.split(' <= '))
        print(str_input, '=', MyFraction(first) <= MyFraction(second))
    if str_input.find(' == ') > 0:
        first, second = (x.strip() for x in str_input.split(' == '))
        print(str_input, '=', MyFraction(first) == MyFraction(second))
    if str_input.find(' != ') > 0:
        first, second = (x.strip() for x in str_input.split(' != '))
        print(str_input, '=', MyFraction(first) != MyFraction(second))
    print('*' * 70)


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
