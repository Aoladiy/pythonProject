from functions import *


show_menu()
while True:
    if r'C:\Users\Aldar\PycharmProjects\pythonProject\directory_for_file_manager' not in os.getcwd():
        print('Выход за допустимые директории')
        os.chdir(r'/my_2_course/network_systems&applications/directory_for_file_manager')
    inp = input('Сделайте выбор >>> ')
    if inp == '!':
        print('Завершение программы')
        break
    elif inp.split()[0] == 'show_menu':
        show_menu()
    elif inp.split()[0] == 'make_directory':
        name = inp.split()[1]
        make_directory(name)
    elif inp.split()[0] == 'remove_directory':
        name = inp.split()[1]
        remove_directory(name)
    elif inp.split()[0] == 'change_directory':
        print('.. - для перехода наверх')
        name = inp.split()[1]
        change_directory(name)
        print('Текущая директория', os.getcwd(), sep='\n')
    elif inp.split()[0] == 'create_file':
        name = inp.split()[1]
        create_file(name)
    elif inp.split()[0] == 'write_file':
        name = inp.split()[1]
        write_file(name)
    elif inp.split()[0] == 'read_file':
        name = inp.split()[1]
        read_file(name)
    elif inp.split()[0] == 'remove_file':
        name = inp.split()[1]
        remove_file(name)
    elif inp.split()[0] == 'copy_file':
        name = inp.split()[1]
        directory = inp.split()[2]
        copy_file(name, directory)
    elif inp.split()[0] == 'replace_file':
        name = inp.split()[1]
        destination = inp.split()[2] + '\\' + name
        replace_file(name, destination)
    elif inp.split()[0] == 'rename_file':
        name = inp.split()[1]
        rename_file(name)
    elif len(inp.split()) == 1:
        print('Нет параметра')
    else:
        print('Неверный ввод')

