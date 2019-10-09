__author__ = 'Ткаченко Кирилл Павлович'


# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import hw05_easy


def change_folder(fld_name):
    if os.path.isabs(fld_name):
        fld_path = fld_name
    else:
        rel_parts = tuple(filter(None, os.path.split(fld_name)))
        fld_path = os.path.join(os.getcwd(), *rel_parts)
    try:
        os.chdir(fld_path)
    except FileNotFoundError:
        print('Error. Folder [{}] does not exist'.format(fld_name))
        return False
    except NotADirectoryError:
        print('Error. [{}] is not a folder'.format(fld_name))
        return False
    print('Folder changed to [{}]'.format(fld_name))
    return True


ACTION_CHOICES = {
    '1': {
        'name': 'Перейти в папку',
        'action': change_folder,
        'user_input': True,
        'param': 'Введите название папки назначения: ',
    },
    '2': {
        'name': 'Просмотреть содержимое текущей папки',
        'action': hw05_easy.list_folder,
        'user_input': False,
        'param': False,
    },
    '3': {
        'name': 'Удалить папку',
        'action': hw05_easy.remove_folder,
        'user_input': True,
        'param': 'Введите название папки для удаления: ',
    },
    '4': {
        'name': 'Создать папку',
        'action': hw05_easy.make_folder,
        'user_input': True,
        'param': 'Введите название создаваемой папки: ',
    },
    '5': {
        'name': 'Закончить работу',
        'action': exit,
        'user_input': False,
        'param': 0,
    },
}


while True:
    print('*' * 80)
    for key, value in ACTION_CHOICES.items():
        print(key, value['name'])
    print('-' * 80)
    user_choice = input('Выберите действие: ')
    print('=' * 80)
    if user_choice in ACTION_CHOICES:
        act = ACTION_CHOICES[user_choice]
        if act['user_input']:
            param = input(act['param'])
        else:
            param = act['param']
        act['action'](param)
    else:
        print('Некорректный ввод')
    