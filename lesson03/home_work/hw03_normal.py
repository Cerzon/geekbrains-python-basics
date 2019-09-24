__author__ = 'Ткаченко Кирилл Павлович'


# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    """
    Подсчёт элементов ряда Фибоначчи с возвращением элементов
    начиная с n и заканчивая m
    """
    prev, curr = (1, 1,)
    result = []
    if n == 1 and m >= 2:
        result = [1, 1,]
    elif n == m == 1 or n == 2:
        result = [1,]
    for i in range(3, m + 1):
        prev, curr = (curr, prev + curr)
        if i >= n:
            result.append(curr)
    return result


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    """
    Принимаем список и возвращаем список, отсортированный по возрастанию
    """
    result = []
    for item in origin_list:
        for i in range(len(result)):
            if item <= result[i]:
                result.insert(i, item)
                break
            if item >= result[len(result) - i - 1]:
                result.insert(len(result) - i, item)
                break
        else:
            result.append(item)
    return result


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def my_filter(*args):
    """
    Возвращаем список (можно бы и просто генератор) с ненулевыми
    и непустыми элементами изначального, либо, при передачи имени
    функции в первом аргументе, если результат выполнения фунцкии
    для элемента ненулевой
    """
    if len(args) == 2:
        func, iter_to_test = args
        return [x for x in iter_to_test if func(x)]
    (iter_to_test,) = args
    return [x for x in iter_to_test if x]


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

