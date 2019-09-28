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
    MyFraction(string)
    |   string - literal representation of the fraction, i.e. '1 1/2', '-3 5/6'
    supports add, sub, mul, truediv, comparison
    """
    def __init__(self, str_fraction, _normalize=True):
        self._negative = False
        self._numerator = 0
        self._denominator = 1
        match = re.match(
            r'^(?P<entier>-?\d+\b)? ?((?P<numerator>(?(entier)|-?)\d+)/(?P<denominator>\d+))?$',
            str_fraction)
        if match is None:
            raise ValueError('Wrong fraction format. "{}" does not match to ' \
                '"[-][<int:entier>] [<int:numerator>/<int:denominator>]"'.format(str_fraction))
        if match.group('numerator'):
            self._negative = int(match.group('numerator')) < 0
            self._numerator = abs(int(match.group('numerator')))
            self._denominator = int(match.group('denominator'))
            if self._denominator == 0:
                raise ValueError("Denominator can't be zero")
        if match.group('entier'):
            self._negative = int(match.group('entier')) < 0
            self._numerator += abs(int(match.group('entier'))) * self._denominator
        if _normalize:
            entier, self._numerator = divmod(self._numerator, self._denominator)
            for i in range(1, self._numerator // 2 + 1):
                if not self._numerator % i and not self._denominator % (self._numerator // i):
                    self._denominator //= self._numerator // i
                    self._numerator = i
                    break
            self._numerator += entier * self._denominator

    def __str__(self):
        str_output = ''
        entier, numerator = divmod(self._numerator, self._denominator)
        if entier and numerator:
            entier *= -1 if self._negative else 1
            str_output = '{0} {1}/{2}'
        elif numerator:
            numerator *= -1 if self._negative else 1
            str_output = '{1}/{2}'
        else:
            entier *= -1 if self._negative else 1
            str_output = '{0}'
        return str_output.format(entier, numerator, self._denominator)

    def __add__(self, other):
        return MyFraction('{0}/{1}'.format(
            (self._numerator * (-1 if self._negative else 1) * other._denominator +
            other._numerator * (-1 if other._negative else 1) * self._denominator),
            self._denominator * other._denominator))

    def __sub__(self, other):
        return MyFraction('{0}/{1}'.format(
            (self._numerator * (-1 if self._negative else 1) * other._denominator -
            other._numerator * (-1 if other._negative else 1) * self._denominator),
            self._denominator * other._denominator))

    def __mul__(self, other):
        return MyFraction('{0}/{1}'.format(
            (self._numerator * (-1 if self._negative else 1) *
            other._numerator * (-1 if other._negative else 1)),
            self._denominator * other._denominator))

    def __truediv__(self, other):
        return MyFraction('{0}/{1}'.format(
            (self._numerator * (-1 if self._negative else 1) *
            other._denominator * (-1 if other._negative else 1)),
            self._denominator * other._numerator))

    def __lt__(self, other):
        return (self._numerator * (-1 if self._negative else 1) * other._denominator
            < other._numerator * (-1 if other._negative else 1) * self._denominator)

    def __le__(self, other):
        return (self._numerator * (-1 if self._negative else 1) * other._denominator
            <= other._numerator * (-1 if other._negative else 1) * self._denominator)

    def __gt__(self, other):
        return (self._numerator * (-1 if self._negative else 1) * other._denominator
            > other._numerator * (-1 if other._negative else 1) * self._denominator)

    def __ge__(self, other):
        return (self._numerator * (-1 if self._negative else 1) * other._denominator
            >= other._numerator * (-1 if other._negative else 1) * self._denominator)

    def __eq__(self, other):
        return (self._numerator * (-1 if self._negative else 1) * other._denominator
            == other._numerator * (-1 if other._negative else 1) * self._denominator)

    def __ne__(self, other):
        return (self._numerator * (-1 if self._negative else 1) * other._denominator
            != other._numerator * (-1 if other._negative else 1) * self._denominator)


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
print('*' * 70)


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


print('*' * 70)
print('Читаем и пишем текстовые файлы')
answer = input('Выполнить чтение списка и запись по отдельным файлам? [Y/N] ').lower()
if answer == 'y' or answer == 'д':
    with open(os.path.join(SCRIPT_DIR, 'data', 'fruits.txt'), 'r', encoding='utf-8') as datafile:
        for fruit in (line.strip('\n') for line in datafile if len(line.strip('\n'))):
            with open(os.path.join(SCRIPT_DIR, 'data', 'fruits_' + fruit[0].upper() + '.txt'), 'a', encoding='utf-8') as fruitfile:
                fruitfile.write(fruit + '\n')
print('*' * 70)
