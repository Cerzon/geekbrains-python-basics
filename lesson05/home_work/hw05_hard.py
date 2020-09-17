__author__ = 'Ткаченко Кирилл Павлович'


# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.


import os
import sys
import shutil

# print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not fso_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    if os.path.isabs(fso_name):
        dir_path = fso_name
    else:
        rel_parts = tuple(filter(None, os.path.split(fso_name)))
        dir_path = os.path.join(os.getcwd(), *rel_parts)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(fso_name))
    except FileExistsError:
        print('директория {} уже существует'.format(fso_name))


def ping():
    print("pong")


def change_dir():
    if not fso_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    if os.path.isabs(fso_name):
        dir_path = fso_name
    else:
        rel_parts = tuple(filter(None, os.path.split(fso_name)))
        dir_path = os.path.join(os.getcwd(), *rel_parts)
    try:
        os.chdir(dir_path)
        print('текущая директория изменена на {}'.format(dir_path))
        print_dir()
    except (FileNotFoundError, NotADirectoryError):
        print('директория {} не найдена'.format(dir_path))


def copy_file():
    if not fso_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    if os.path.isabs(fso_name):
        src_path = fso_name
    else:
        rel_parts = tuple(filter(None, os.path.split(fso_name)))
        src_path = os.path.join(os.getcwd(), *rel_parts)
    if os.path.isfile(src_path):
        dst_name = 'copy_' + os.path.split(fso_name)[-1]
        dst_path = os.path.join(os.path.dirname(src_path), dst_name)
        shutil.copy(src_path, dst_path)
        print('файл скопирован в {}'.format(dst_name))
    else:
        print('{} не является файлом'.format(fso_name))


def remove_file():
    if not fso_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    if os.path.isabs(fso_name):
        tgt_path = fso_name
    else:
        rel_parts = tuple(filter(None, os.path.split(fso_name)))
        tgt_path = os.path.join(os.getcwd(), *rel_parts)
    if os.path.isfile(tgt_path):
        while True:
            answer = input('Удалить файл {}? [<Y>es(<Д>a)/<N>o(<Н>ет)] '.format(fso_name))
            if answer in 'YyДд':
                break
            elif answer in 'NnНн':
                print('Удаление {} отменено'.format(fso_name))
                return
        try:
            os.remove(tgt_path)
        except PermissionError:
            print('невозможно удалить {} - файл занят другим процессом'.format(fso_name))
            return
        print('файл {} успешно удалён'.format(fso_name))
    else:
        print('{} не является файлом'.format(fso_name))


def print_dir():
    print(os.getcwd())


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": remove_file,
    "cd": change_dir,
    "ls": print_dir,
}

try:
    fso_name = sys.argv[2]
except IndexError:
    fso_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if key in do:
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
