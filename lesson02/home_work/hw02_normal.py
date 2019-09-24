__author__ = 'Ткаченко Кирилл Павлович'


# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]


from math import sqrt


if __name__ == '__main__':
    print('*' * 70)
    print('Составляем список из квадратных корней,')
    print('представляющих из себя вещественные целые числа')
    print('-' * 70)
    input_list = [int(x.strip()) for x in input('Введите список целых чисел через запятую: ').split(',')]
    print([int(sqrt(x)) for x in input_list if x >= 0 and not sqrt(x) % 1])
    print('*' * 70)


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)


def date_humanized(str_date):
    DAY_NAME = (
        'первое',
        'второе',
        'третье',
        'четвёртое',
        'пятое',
        'шестое',
        'седьмое',
        'восьмое',
        'девятое',
        'десятое',
        'одиннадцатое',
        'двенадцатое',
        'тринадцатое',
        'четырнадцатое',
        'пятнадцатое',
        'шестнадцатое',
        'семнадцатое',
        'восемнадцатое',
        'девятнадцатое',
        'двадцатое',
        'двадцать первое',
        'двадцать второе',
        'двадцать третье',
        'двадцать четвёртое',
        'двадцать пятое',
        'двадцать шестое',
        'двадцать седьмое',
        'двадцать восьмое',
        'двадцать девятое',
        'тридцатое',
        'тридцать первое',
    )
    MONTH_INFO = (
        {'name': 'января', 'limit': 31,},
        {'name': 'февраля', 'limit': 29,},
        {'name': 'марта', 'limit': 31,},
        {'name': 'апреля', 'limit': 30,},
        {'name': 'мая', 'limit': 31,},
        {'name': 'июня', 'limit': 30,},
        {'name': 'июля', 'limit': 31,},
        {'name': 'августа', 'limit': 31,},
        {'name': 'сентября', 'limit': 30,},
        {'name': 'октября', 'limit': 31,},
        {'name': 'ноября', 'limit': 30,},
        {'name': 'декабря', 'limit': 31,},
    )
    iday, imonth, iyear = (int(x) if x.isnumeric() else -1 for x in str_date.split('.'))
    if iday < 1 or imonth < 1 or imonth > 12 or iyear < 1:
        return 'Дата введена неправильно'
    if iday > MONTH_INFO[imonth - 1]['limit']:
        return 'Дата введена неправильно'
    if imonth == 2 and iyear % 4 and iday == MONTH_INFO[imonth - 1]['limit']:
        return 'Дата введена неправильно'
    return '{0} {1} {2} года'.format(DAY_NAME[iday - 1], MONTH_INFO[imonth - 1]['name'], iyear)


if __name__ == '__main__':
    print('*' * 70)
    print('Переводим даты из чисел в слова')
    print('-' * 70)
    in_date = input('Введите дату в формате dd.mm.yyyy: ')
    print(date_humanized(in_date))
    print('*' * 70)


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random


from random import randint

if __name__ == '__main__':
    print('*' * 70)
    print('Заполняем список из n элементов случайными числами в диапазоне от -100 до 100')
    print('-' * 70)
    n_size = int(input('Введите количество элементов n: '))
    print([randint(-100, 100) for x in range(n_size)])
    print('*' * 70)


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]


if __name__ == '__main__':
    print('*' * 70)
    print('Списки с повторяющимися элементами')
    input_list = [int(x.strip()) for x in input('Введите список целых чисел через запятую: ').split(',')]
    print('-' * 70)
    print('Составляем из исходного список без повторов')
    print([input_list[i] for i in range(len(input_list)) if not input_list[i] in input_list[:i]])
    print('-' * 70)
    print('Составляем из исходного список из неповторяющихся элементов')
    print([x for x in input_list if not x in input_list[input_list.index(x) + 1:]])
    print('*' * 70)
