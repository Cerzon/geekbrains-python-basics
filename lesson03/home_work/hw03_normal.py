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
        result = [1, 1]
    elif n == m == 1 or n == 2:
        result = [1]
    for i in range(3, m + 1):
        prev, curr = (curr, prev + curr,)
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


def my_filter(func_name, array):
    """
    my_filter(function or None, iterable)
    -------------------------------------------------
    Возвращаем список (хотя в оригинале просто генератор) с
    ненулевыми и непустыми элементами изначального,
    либо, при передачи имени функции в первом аргументе,
    если результат выполнения фунцкии для элемента
    не нулевой/ложный/None
    """
    if func_name is None:
        return [x for x in array if bool(x)]
    else:
        return [x for x in array if func_name(x)]
    


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def check_points(point1, point2, point3, point4):
    """
    point = tuple(x, y)
    Проверка, являются ли переданные функции точки
    вершинами параллелограмма
    """
    if (point1 == point2 or point1 == point3 or
            point1 == point4 or point2 == point3 or
            point2 == point4 or point3 == point4):
        return False
    if ((point1[0] + point2[0] == point3[0] + point4[0] and
            point1[1] + point2[1] == point3[1] + point4[1]) or
            (point1[0] + point3[0] == point2[0] + point4[0] and
            point1[1] + point3[1] == point2[1] + point4[1]) or
            (point1[0] + point4[0] == point2[0] + point3[0] and
            point1[1] + point4[1] == point2[1] + point3[1])):
        return True
    else:
        return False
