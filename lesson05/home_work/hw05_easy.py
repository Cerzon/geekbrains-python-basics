__author__ = 'Ткаченко Кирилл Павлович'


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os


def make_folder(fld_name):
    """
    Создаёт в текущей папку с заданным именем, если такой папки ещё нет.
    """
    if os.path.exists(fld_name) and os.path.isdir(fld_name):
        print('Folder {} already exists'.format(fld_name))
        return False
    elif not os.path.isdir(os.path.dirname(fld_name)):
        print('Parent folder {} does not exist'.format(os.path.dirname(fld_name)))
        return False
    os.mkdir(fld_name)
    print('Folder {} created'.format(fld_name))
    return True


def remove_folder(fld_name):
    """
    Удаляет из текущей папку с заданным именем, если такая папка есть.
    """
    if os.path.isdir(fld_name):
        if os.listdir(fld_name):
            print('Folder {} is not empty'.format(fld_name))
            return False
        os.rmdir(fld_name)
        print('Folder {} deleted'.format(fld_name))
        return True
    print('Folder {} does not exist'.format(fld_name))
    return False


# создаём папки dir_1 - dir_9 в папке, из которой запущен скрипт
# name_tpl = os.path.join(os.getcwd(), 'dir_')
# for folder_name in (name_tpl + str(x) for x in range(1, 10)):
#     make_folder(folder_name)

# print('*' * 80)

# # удаляем папки dir_1 - dir_9 в папке, из которой запущен скрипт
# for folder_name in (name_tpl + str(x) for x in range(1, 10)):
#     remove_folder(folder_name)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_folder(fld_name=os.curdir, folders_only=False):
    """
    Выводит содержимое папки с заданным именем.
    folders_only=True -- вывести только имена папок.
    """
    if not os.path.isabs(fld_name):
        fld_name = os.path.join(os.path.abspath(os.curdir), fld_name)
    if os.path.isdir(fld_name) and os.listdir(fld_name):
        for name in os.listdir(fld_name):
            if os.path.isdir(os.path.join(fld_name, name)):
                print('[{}]'.format(name))
            elif not folders_only:
                print(name)


print('*' * 80)

list_folder(folders_only=True)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
