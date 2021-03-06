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


print('*' * 70)
print('Вывод выровненного списка')
print('-' * 70)
input_list = [x.strip() for x in input('Введите список через запятую: ').split(',')]
num_wdth = len(str(len(input_list) + 1))
val_wdth = max(len(x) for x in input_list)
for i, item_value in enumerate(input_list, 1):
    print('{0:>{nw}}. {1:>{vw}}'.format(i, item_value, nw=num_wdth, vw=val_wdth))
print('*' * 70)


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

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


print('*' * 70)
print('Составляем список из исходного списка целых чисел')
print('-' * 70)
input_list = [
    int(x.strip()) if x.strip().isnumeric() or x.strip()[1:].isnumeric()
    else None for x in input('Введите список целых чисел через запятую: ').split(',')]
while None in input_list:
    input_list.remove(None)
print([x * 2 if x % 2 else x / 4 for x in input_list])
print('*' * 70)
