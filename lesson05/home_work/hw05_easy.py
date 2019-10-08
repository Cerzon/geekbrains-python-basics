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
        print('Error. Folder [{}] already exists'.format(fld_name))
        return False
    except FileNotFoundError:
        print('Error. Parent folder [{}] does not exist'.format(os.path.dirname(fld_name)))
        return False
    print('Folder [{}] created'.format(fld_name))
    return True


def remove_folder(fld_name):
    """
    Удаляет из текущей папку с заданным именем, если такая папка есть.
    """
    try:
        os.rmdir(fld_name)
    except NotADirectoryError:
        print('Error. [{}] is not a folder'.format(fld_name))
        return False
    except FileNotFoundError:
        print('Error. Folder [{}] does not exist'.format(fld_name))
        return False
    except OSError:
        print('Error. Folder [{}] is not empty'.format(fld_name))
        return False
    print('Folder [{}] deleted'.format(fld_name))
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

def list_folder(folders_only=False):
    """
    folders_only=True -- вывести только имена папок.
    """
    fldr_count = 0
    file_count = 0
    if os.listdir(os.curdir):
        for name in os.listdir(os.curdir):
            if os.path.isdir(name):
                print('[{}]'.format(name))
                fldr_count += 1
            elif not folders_only:
                print(name)
                file_count += 1
    else:
        print('-- empty --')
    print('Total:', end=' ')
    if not folders_only:
        print('{} files,'.format(file_count), end=' ')
    print('{} folders'.format(fldr_count))


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