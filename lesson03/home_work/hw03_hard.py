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
    def __init__(self, str_fraction):
        match = re.match(
            r'^(?P<entier>-?\d+\b)? ?((?P<dividend>(?(entier)|-?)\d+)/(?P<divider>\d+))?$',
            str_fraction)
        if match is None:
            return None
        self.negative = False
        self.entier = 0
        self.dividend = 0
        self.divider = 1
        if match.group('entier'):
            self.entier = int(match.group('entier'))
            if self.entier < 0:
                self.negative = True
                self.entier *= -1
        if match.group('dividend'):
            self.dividend = int(match.group('dividend'))
            if self.dividend < 0:
                self.negative = True
                self.dividend *= -1
            self.divider = int(match.group('divider'))
            if self.divider == 0:
                raise ZeroDivisionError
        self.simplify()

    def simplify(self):
        self.entier += self.dividend // self.divider
        self.dividend = self.dividend % self.divider
        for i in range(1, self.dividend // 2):
            if not self.dividend % i and not self.divider % (self.dividend // i):
                self.divider //= self.dividend // i
                self.dividend = i
                break
        if self.dividend == 0:
            self.divider = 1

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
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass


var1 = MyFraction('-54 125/36')
print(var1)
print('-' * 70)
var1 = MyFraction('3 5/55')
print(var1)
print('-' * 70)
var1 = MyFraction('-144/24')
print(var1, var1.dividend, var1.divider)

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
