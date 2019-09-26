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
        self._negative = False
        self._entier = 0
        self._dividend = 0
        self._divider = 1
        if isinstance(args[0], str):
            match = re.match(
                r'^(?P<entier>-?\d+\b)? ?((?P<dividend>(?(entier)|-?)\d+)/(?P<divider>\d+))?$',
                args[0])
            if match is None:
                raise ValueError('Wrong fraction format. "{}" does not match to "[-][<int:entier>] [<int:dividend>/<int:divider>]"'.format(args[0]))
            if match.group('entier'):
                self._entier = int(match.group('entier'))
            if match.group('dividend'):
                self._dividend = int(match.group('dividend'))
                self._divider = int(match.group('divider'))
        elif len(args) == 3 and not False in (isinstance(x, int) for x in args):
            self._entier, self._dividend, self._divider = args
            if self._divider < 0:
                raise ValueError('Wrong fraction format. Divider must be positive')
        else:
            return None
        if self._divider == 0:
            raise ValueError('Divider can not be zero')
        if self._entier < 0:
            self._negative = True
            self._entier *= -1
        if self._dividend < 0:
            self._negative = True
            self._dividend *= -1
        self.simplify()

    def simplify(self):
        self._entier += self._dividend // self._divider
        self._dividend = self._dividend % self._divider
        for i in range(1, self._dividend // 2 + 1):
            if not self._dividend % i and not self._divider % (self._dividend // i):
                self._divider //= self._dividend // i
                self._dividend = i
                break
        if self._dividend == 0:
            self._divider = 1

    def complicate(self):
        self._dividend += self._entier * self._divider
        self._entier = 0

    def __str__(self):
        str_output = ''
        if self._entier:
            str_output = str(self._entier * (-1 if self._negative else 1))
        if self._dividend:
            if len(str_output):
                str_output += ' '
            else:
                str_output = '-' if self._negative else ''
            str_output += '{0}/{1}'.format(self._dividend, self._divider)
        return str_output

    def __add__(self, other):
        if not isinstance(other, MyFraction):
            if isinstance(other, int):
                other = MyFraction(other, 0, 1)
            else:
                return NotImplemented
        self.complicate()
        other.complicate()
        res_dividend = self._dividend * (-1 if self._negative else 1) * other._divider + other._dividend * (-1 if other._negative else 1) * self._divider
        self.simplify()
        other.simplify()
        return MyFraction(0, res_dividend, self._divider * other._divider)

    def __sub__(self, other):
        if not isinstance(other, MyFraction):
            if isinstance(other, int):
                other = MyFraction(other, 0, 1)
            else:
                return NotImplemented
        self.complicate()
        other.complicate()
        res_dividend = self._dividend * (-1 if self._negative else 1) * other._divider - other._dividend * (-1 if other._negative else 1) * self._divider
        self.simplify()
        other.simplify()
        return MyFraction(0, res_dividend, self._divider * other._divider)

    def __mul__(self, other):
        if not isinstance(other, MyFraction):
            if isinstance(other, int):
                other = MyFraction(other, 0, 1)
            else:
                return NotImplemented
        self.complicate()
        other.complicate()
        res_dividend = self._dividend * (-1 if self._negative else 1) * other._dividend * (-1 if other._negative else 1)
        self.simplify()
        other.simplify()
        return MyFraction(0, res_dividend, self._divider * other._divider)

    def __truediv__(self, other):
        if not isinstance(other, MyFraction):
            if isinstance(other, int):
                other = MyFraction(other, 0, 1)
            else:
                return NotImplemented
        self.complicate()
        other.complicate()
        res_dividend = self._dividend * (-1 if self._negative else 1) * other._divider * (-1 if other._negative else 1)
        res_divider = self._divider * other._dividend
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
        result = self._dividend * (-1 if self._negative else 1) * other._divider < other._dividend * (-1 if other._negative else 1) * self._divider
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
        result = self._dividend * (-1 if self._negative else 1) * other._divider <= other._dividend * (-1 if other._negative else 1) * self._divider
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
        result = self._dividend * (-1 if self._negative else 1) * other._divider > other._dividend * (-1 if other._negative else 1) * self._divider
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
        result = self._dividend * (-1 if self._negative else 1) * other._divider >= other._dividend * (-1 if other._negative else 1) * self._divider
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
        result = self._dividend * (-1 if self._negative else 1) * other._divider == other._dividend * (-1 if other._negative else 1) * self._divider
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
        result = self._dividend * (-1 if self._negative else 1) * other._divider != other._dividend * (-1 if other._negative else 1) * self._divider
        self.simplify()
        other.simplify()
        return result


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


import os


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


if __name__ == '__main__':
    print('*' * 70)
    print('Считаем отработанное время и чужие деньги')
    answer = input('Выполнить чтение данных из файлов и расчёт? [Y/N] ').lower()
    if answer == 'y' or answer == 'д':
        employee_list = []
        pattern = re.compile(r'^([а-яА-Я]+\b)[ \t]+(\b[-а-яА-Я]+\b)[ \t]+(\b\d+\b)[ \t]+(\b[-а-яА-Я]+\b)[ \t]+(\b\d+)$')
        with open(os.path.join(SCRIPT_DIR, 'data', 'workers'), 'r', encoding='utf-8') as employees:
            for record in (line.strip('\n ') for line in employees if len(line.strip('\n '))):
                match = pattern.match(record)
                if match:
                    employee_list.append(dict(zip(
                        ('first_name', 'last_name', 'salary', 'position', 'hours',),
                        (int(x) if x.isnumeric() else x for x in match.groups(default=None)))))

        with open(os.path.join(SCRIPT_DIR, 'data', 'hours_of'), 'r', encoding='utf-8') as worked_hours:
            for record in (line.strip('\n ') for line in worked_hours if len(line.strip('\n '))):
                for employee in employee_list:
                    if (employee['first_name'] in record and
                        employee['last_name'] in record):
                        match = re.match(
                            r'^{0}[ \t]+{1}[ \t]+(\b\d+)$'.format(employee['first_name'],
                                employee['last_name']), record)
                        employee['worked_out'] = int(match.group(1))
                        employee['pay_out'] = int(employee['salary'] * (
                            1 + (employee['worked_out'] / employee['hours'] - 1) * (
                                2 if employee['worked_out'] > employee['hours'] else 1)))

        # fn_wdth = max(len(emval) for emp in employee_list for emkey, emval in emp.items() if emkey == 'first_name')
        # ln_wdth = max(len(emval) for emp in employee_list for emkey, emval in emp.items() if emkey == 'last_name')
        # ps_wdth = max(len(emval) for emp in employee_list for emkey, emval in emp.items() if emkey == 'position')
        # sl_wdth = max(len(str(emval)) for emp in employee_list for emkey, emval in emp.items() if emkey == 'salary')
        # hr_wdth = max(len(str(emval)) for emp in employee_list for emkey, emval in emp.items() if emkey == 'hours')
        # wo_wdth = max(len(str(emval)) for emp in employee_list for emkey, emval in emp.items() if emkey == 'worked_out')
        # po_wdth = max(len(str(emval)) for emp in employee_list for emkey, emval in emp.items() if emkey == 'pay_out')
        # for employee in employee_list:
        #     print(
        #         '{0:<{fn_wdth}} {1:<{ln_wdth}}  {2:<{ps_wdth}}  {3:>{sl_wdth}}  {4:>{hr_wdth}}  {5:>{wo_wdth}}  {6:>{po_wdth}}'.format(
        #             employee['first_name'],
        #             employee['last_name'],
        #             employee['position'],
        #             employee['salary'],
        #             employee['hours'],
        #             employee['worked_out'],
        #             employee['pay_out'],
        #             fn_wdth=fn_wdth,
        #             ln_wdth=ln_wdth,
        #             ps_wdth=ps_wdth,
        #             sl_wdth=sl_wdth,
        #             hr_wdth=hr_wdth,
        #             wo_wdth=wo_wdth,
        #             po_wdth=po_wdth
        #         )
        #     )


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


if __name__ == '__main__':
    print('*' * 70)
    print('Читаем и пишем текстовые файлы')
    answer = input('Выполнить чтение списка и запись по отдельным файлам? [Y/N] ').lower()
    if answer == 'y' or answer == 'д':
        with open(os.path.join(SCRIPT_DIR, 'data', 'fruits.txt'), 'r', encoding='utf-8') as datafile:
            for fruit in (line.strip('\n') for line in datafile if len(line.strip('\n'))):
                with open(os.path.join(SCRIPT_DIR, 'data', 'fruits_' + fruit[0].upper() + '.txt'), 'a', encoding='utf-8') as fruitfile:
                    fruitfile.write(fruit + '\n')
    print('*' * 70)
