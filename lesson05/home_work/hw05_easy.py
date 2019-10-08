__author__ = 'Ткаченко Кирилл Павлович'


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil


def make_folder(fld_name):
    """
    Создаёт в текущей папку с заданным именем, если такой папки ещё нет.
    """
    try:
        os.mkdir(fld_name)
    except FileExistsError:
        print('Folder {} already exists'.format(fld_name))
        return False
    except FileNotFoundError:
        print('Parent folder {} does not exist'.format(os.path.dirname(fld_name)))
        return False
    print('Folder {} created'.format(fld_name))
    return True


def remove_folder(fld_name):
    """
    Удаляет из текущей папку с заданным именем, если такая папка есть.
    """
    try:
        os.rmdir(fld_name)
    except NotADirectoryError:
        print('{} is not a folder'.format(fld_name))
        return False
    except FileNotFoundError:
        print('Folder {} does not exist'.format(fld_name))
        return False
    except OSError:
        print('Folder {} is not empty'.format(fld_name))
        return False
    print('Folder {} deleted'.format(fld_name))
    return True



if __name__ == '__main__':
    # создаём папки dir_1 - dir_9 в папке, из которой запущен скрипт
    for folder_name in ('dir_' + str(x) for x in range(1, 10)):
        make_folder(folder_name)

    print('*' * 80)

    # удаляем папки dir_1 - dir_9 в папке, из которой запущен скрипт
    for folder_name in ('dir_' + str(x) for x in range(1, 10)):
        remove_folder(folder_name)


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


if __name__ == '__main__':

    print('*' * 80)

    list_folder(folders_only=True)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

if __name__ == '__main__':

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

    # копируем встроенными средствами
    dest_name = 'copy_' + os.path.split(__file__)[-1]
    with open(os.path.abspath(__file__), 'r', encoding='utf-8') as src:
        with open(os.path.join(SCRIPT_DIR, dest_name), 'w', encoding='utf-8') as dst:
            dst.writelines(src.readlines())

    # пользуемся библиотекой shell util
    dest_name = 'copy_' + dest_name
    shutil.copy(os.path.abspath(__file__), os.path.join(SCRIPT_DIR, dest_name))