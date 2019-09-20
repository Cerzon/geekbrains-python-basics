__author__ = 'Ткаченко Кирилл Павлович'

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()


def aligned_print(value_list):
    """
    Вывод выровненного по правой стороне
    нумерованного списка
    """
    num_wdth = len(str(len(value_list) + 1))
    val_wdth = max([len(x) for x in value_list])
    for i in range(len(value_list)):
        print('{0:>{nw}}. {1:>{vw}}'.format(i + 1, value_list[i], nw=num_wdth, vw=val_wdth))


if __name__ == '__main__':
    print('*' * 70)
    print('Вывод выровненного списка')
    print('-' * 70)
    input_list = [x.strip() for x in input('Введите список через запятую: ').split(',')]
    aligned_print(input_list)
    print('*' * 70)


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

if __name__ == '__main__':
    print('*' * 70)
    print('Удаление элементов из списка')
    print('-' * 70)
    input_list = [x.strip() for x in input('Введите начальный список через запятую: ').split(',')]
    input_list_to_remove = [x.strip() for x in input('Введите список удаляемых элементов через запятую: ').split(',')]
    print('-' * 70)
    for elem in input_list_to_remove:
        while elem in input_list:
            input_list.remove(elem)
    print('Начальный список с удалёнными элементами:')
    print(input_list)
    print('*' * 70)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.


if __name__ == '__main__':
    print('*' * 70)
    print('Составляем список из исходного списка целых чисел')
    print('-' * 70)
    input_list = [int(x.strip()) for x in input('Введите список целых чисел через запятую: ').split(',')]
    print([x * 2 if x % 2 else x / 4 for x in input_list])
    print('*' * 70)
