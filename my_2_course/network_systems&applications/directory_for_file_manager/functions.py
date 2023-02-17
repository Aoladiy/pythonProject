import os
import shutil


def show_menu():
    print('! - выйти из программы')
    print('show_menu - Вывести меню ещё раз')
    print('make_directory - создание папки')
    print('remove_directory - удаление папки')
    print('change_directory - переместиться')
    print('create_file - создать файл')
    print('write_file - записать текст в файл')
    print('read_file - просмотреть содержимое файла')
    print('remove_file - удалить файл')
    print('copy_file - копировать файл')
    print('replace_file - переместить файл')
    print('rename_file - переименовать файл')


def make_directory(name):
    if not os.path.isdir(name):
        os.mkdir(name)
        return print(f'Создана папка {name}')
    else:
        print('!!!Такая папка уже существует!!!')


def remove_directory(name):
    if not os.path.isdir(name):
        print('!!!Такой папки не существует!!!')
    else:
        os.rmdir(name)
        return print(f'Папка {name} удалена')


def change_directory(name):
    if not os.path.isdir(name):
        print('!!!Такой папки не существует!!!')
    else:
        os.chdir(name)


def create_file(name):
    if name[-4:] != '.txt':
        name += '.txt'
    if not os.path.isfile(name):
        with open(name, 'w') as file:
            return print(f'Создан файл {file.name}')
    else:
        print('!!!Такой файл уже существует!!!')


def write_file(name):
    if name[-4:] != '.txt':
        name += '.txt'
    if os.path.isfile(name):
        with open(name, 'w') as file:
            text = input('Введите текст >>> ')
            file.write(text)
            return print(f'Текст записан в файл {file.name}')
    else:
        print('!!!Такого файла не существует!!!')


def read_file(name):
    if name[-4:] != '.txt':
        name += '.txt'
    if os.path.isfile(name):
        with open(name) as file:
            return print(file.read())
    else:
        print('!!!Такого файла не существует!!!')


def remove_file(name):
    if name[-4:] != '.txt':
        name += '.txt'
    if os.path.isfile(name):
        os.remove(name)
        return print(f'файл {name} удалён')
    else:
        print('!!!Такого файла не существует!!!')


def copy_file(name, directory):
    if name[-4:] != '.txt':
        name += '.txt'
    if os.path.isfile(name):
        if os.path.isdir(directory):
            shutil.copy(name, directory)
            return print(f'Файл {name} скопирован в папку {directory}')
    else:
        print('!!!Такого файла или директории не существует!!!')


def replace_file(name, destination):
    if name[-4:] != '.txt':
        name += '.txt'
    if destination[-4:] != '.txt':
        destination += '.txt'
    if os.path.isfile(name):
        os.replace(name, destination)
    else:
        print('!!!Такого файла или директории не существует!!!')


def rename_file(name):
    if name[-4:] != '.txt':
        name += '.txt'
    if os.path.isfile(name):
        new = input('Новое имя >>> ')
        if new[-4:] != '.txt':
            new += '.txt'
        os.rename(name, new)
        return print(f'Файл {name} переименован в {new}')
    else:
        print('!!!Такого файла или директории не существует!!!')
