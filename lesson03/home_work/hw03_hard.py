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
    def __init__(self, str_fraction):
        self._neg = False
        self._num = 0
        self._den = 1
        match = re.match(
            r'^(?P<entier>-?\d+\b)? ?((?P<numerator>(?(entier)|-?)\d+)/(?P<denominator>\d+))?$',
            str_fraction)
        if match is None:
            raise ValueError('Wrong fraction format. "{}" does not match to ' \
                '"[-][<int:entier>] [<int:numerator>/<int:denominator>]"'.format(str_fraction))
        if match.group('numerator'):
            self._neg = int(match.group('numerator')) < 0
            self._num = abs(int(match.group('numerator')))
            self._den = int(match.group('denominator'))
            if self._den == 0:
                raise ValueError("Denominator can't be zero")
        if match.group('entier'):
            self._neg = int(match.group('entier')) < 0
            self._num += abs(int(match.group('entier'))) * self._den
        entier, self._num = divmod(self._num, self._den)
        for i in range(1, self._num // 2 + 1):
            if not self._num % i and not self._den % (self._num // i):
                self._den //= self._num // i
                self._num = i
                break
        self._num += entier * self._den

    def __str__(self):
        str_output = ''
        entier, numerator = divmod(self._num, self._den)
        if entier and numerator:
            entier *= -1 if self._neg else 1
            str_output = '{0} {1}/{2}'
        elif numerator:
            numerator *= -1 if self._neg else 1
            str_output = '{1}/{2}'
        else:
            entier *= -1 if self._neg else 1
            str_output = '{0}'
        return str_output.format(entier, numerator, self._den)

    def __add__(self, other):
        return MyFraction('{0}/{1}'.format(
            (self._num * (-1 if self._neg else 1) * other._den +
            other._num * (-1 if other._neg else 1) * self._den),
            self._den * other._den))

    def __sub__(self, other):
        return MyFraction('{0}/{1}'.format(
            (self._num * (-1 if self._neg else 1) * other._den -
            other._num * (-1 if other._neg else 1) * self._den),
            self._den * other._den))

    def __mul__(self, other):
        return MyFraction('{0}/{1}'.format(
            (self._num * (-1 if self._neg else 1) *
            other._num * (-1 if other._neg else 1)),
            self._den * other._den))

    def __truediv__(self, other):
        return MyFraction('{0}/{1}'.format(
            (self._num * (-1 if self._neg else 1) *
            other._den * (-1 if other._neg else 1)),
            self._den * other._num))

    def __lt__(self, other):
        return (self._num * (-1 if self._neg else 1) * other._den
            < other._num * (-1 if other._neg else 1) * self._den)

    def __le__(self, other):
        return (self._num * (-1 if self._neg else 1) * other._den
            <= other._num * (-1 if other._neg else 1) * self._den)

    def __gt__(self, other):
        return (self._num * (-1 if self._neg else 1) * other._den
            > other._num * (-1 if other._neg else 1) * self._den)

    def __ge__(self, other):
        return (self._num * (-1 if self._neg else 1) * other._den
            >= other._num * (-1 if other._neg else 1) * self._den)

    def __eq__(self, other):
        return (self._num * (-1 if self._neg else 1) * other._den
            == other._num * (-1 if other._neg else 1) * self._den)

    def __ne__(self, other):
        return (self._num * (-1 if self._neg else 1) * other._den
            != other._num * (-1 if other._neg else 1) * self._den)


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


# print('*' * 70)
# print('Считаем отработанное время и чужие деньги')
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
            if (employee['first_name'] in record and employee['last_name'] in record):
                match = re.search(r'\b\d+$', record)
                employee['worked_out'] = int(match.group(0))
                diff_modifier = 1
                if employee['worked_out'] > employee['hours']:
                    diff_modifier = 2
                employee['pay_out'] = int(employee['salary'] * 
                    (1 + (employee['worked_out'] / employee['hours'] - 1) * diff_modifier))

# fn_wdth = max(len(emval) for emp in employee_list for emkey, emval in emp.items() if emkey == 'first_name')
# ln_wdth = max(len(emval) for emp in employee_list for emkey, emval in emp.items() if emkey == 'last_name')
# ps_wdth = max(len(emval) for emp in employee_list for emkey, emval in emp.items() if emkey == 'position')
# sl_wdth = max(len(str(emval)) for emp in employee_list for emkey, emval in emp.items() if emkey == 'salary')
# hr_wdth = max(len(str(emval)) for emp in employee_list for emkey, emval in emp.items() if emkey == 'hours')
# wo_wdth = max(len(str(emval)) for emp in employee_list for emkey, emval in emp.items() if emkey == 'worked_out')
# po_wdth = max(len(str(emval)) for emp in employee_list for emkey, emval in emp.items() if emkey == 'pay_out')
# for employee in employee_list:
#     print(
#         '{0} {1}  {2}  {3}  {4}  {5}  {6}'.format(
#             employee['first_name'].ljust(fn_wdth),
#             employee['last_name'].ljust(ln_wdth),
#             employee['position'].ljust(ps_wdth),
#             str(employee['salary']).rjust(sl_wdth),
#             str(employee['hours']).rjust(hr_wdth),
#             str(employee['worked_out']).rjust(wo_wdth),
#             str(employee['pay_out']).rjust(po_wdth),
#         )
#     )
# print('*' * 70)


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
with open(os.path.join(SCRIPT_DIR, 'data', 'fruits.txt'), 'r', encoding='utf-8') as datafile:
    for fruit in (line.strip('\n') for line in datafile if len(line.strip('\n'))):
        output_name = os.path.join(SCRIPT_DIR, 'data', 'fruits_' + fruit[0].upper() + '.txt')
        with open(output_name, 'a', encoding='utf-8') as fruitfile:
            fruitfile.write(fruit + '\n')
print('*' * 70)
