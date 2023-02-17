# r = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
russian_alphabet = [
    ["а", "б", "в", "г", "д", "е"],
    ["ё", "ж", "з", "и", "й", "к"],
    ["л", "м", "н", "о", "п", "р"],
    ["с", "т", "у", "ф", "х", "ц"],
    ["ч", "ш", "щ", "ъ", "ы", "ь"],
    ["э", "ю", "я", "-", "+", "="]
]

# l = "abcdefghijklmnopqrstuvwxyz"
latin_alphabet = [
    ['a', 'b', 'c', 'd', 'e'],
    ['f', 'g', 'h', 'i', 'k'],
    ['l', 'm', 'n', 'o', 'p'],
    ['q', 'r', 's', 't', 'u'],
    ['v', 'w', 'x', 'y', 'z']
]


def show_menu():
    print("Шифровка и расшифровка по квадрату Поллибия")
    print("exit, чтобы выйти")
    print("menu, чтобы показать меню")
    print("1 en, чтобы зашифровать первым методом")
    print("1 de, чтобы дешифровать первым методом")
    print("2 en, чтобы зашифровать вторым методом")
    print("2 de, чтобы дешифровать вторым методом")
    print("3 en, чтобы зашифровать третьим методом")
    print("4 de, чтобы дешифровать третьим методом")
    print()


def what_alphabet(to_check):
    for line in russian_alphabet:
        if to_check[0] in line:
            alphabet = russian_alphabet
            return alphabet
    for line in latin_alphabet:
        if to_check[0] in line:
            alphabet = latin_alphabet
            return alphabet



def first_encoding(to_encode):
    # определение алфавита
    alphabet = what_alphabet(to_encode)

    # шифровка (сдвиг символов сообщения на 1 линию вниз по алфавиту)
    encoded = [""] * len(to_encode)
    for line_index in range(len(alphabet)):
        line = alphabet[line_index]
        next_line = alphabet[(line_index + 1) % len(alphabet)]

        index_in_to_encoded = 0
        for char_to_encode in to_encode:
            if char_to_encode in line:
                # print("буква >>>", char_to_encode)  # буква
                encoded_char = next_line["".join(line).index(char_to_encode)]
                if encoded_char:
                    encoded[index_in_to_encoded] = encoded_char
                    # print("в букву >>>", encoded[index_in_to_encoded])  # в букву
                else:
                    encoded[index_in_to_encoded] = alphabet[(line_index + 2) % len(alphabet)][
                        "".join(line).index(char_to_encode)]
                    # print("в букву >>>", encoded[index_in_to_encoded])  # в букву
                # print()
            index_in_to_encoded += 1
    return to_encode, "".join(encoded)


def second_encoding(to_encode):
    # определение алфавита
    alphabet = what_alphabet(to_encode)

    # координаты записываются вертикально(получаем список координат в виде кортежей)
    encoded = [()] * len(to_encode)
    for line_index in range(len(alphabet)):
        index_in_to_encoded = 0
        for char_to_encode in to_encode:
            if char_to_encode in alphabet[line_index]:
                encoded[index_in_to_encoded] = alphabet[line_index].index(char_to_encode) + 1, line_index + 1
                # print(char_to_encode, alphabet[line_index].index(char_to_encode), line_index) # буква, горизонталь, вертикаль
            index_in_to_encoded += 1

    # код чтобы посмотреть координаты в удобном формате
    # первая строка - горизонтальные координаты, а вторая - вертикальные
    # print()
    # horizontal = []
    # vertical = []
    # for element in encoded:
    #     horizontal.append(element[0])
    #     vertical.append(element[1])
    # print(horizontal)
    # print(vertical)
    # print()

    # а затем считываются построчно (получаем одномерный список)
    coords = []
    for element in encoded:
        if element:
            coords.append(element[0])
    for element in encoded:
        if element:
            coords.append(element[1])

    # разбивка получившегося списка на координаты (получаем список координат в виде кортежей)
    coords = [coords[i:i + 2] for i in range(0, len(coords), 2)]

    # считывание координат
    result = [""] * len(coords)
    index_of_char = 0
    for element in coords:
        result[index_of_char] = alphabet[element[1] - 1][element[0] - 1]
        index_of_char += 1

    return to_encode, "".join(result)


def third_encoding(to_encode, shift=1):
    # определение алфавита
    alphabet = what_alphabet(to_encode)

    # координаты записываются вертикально (получаем список координат в виде кортежей)
    encoded = [()] * len(to_encode)
    for line_index in range(len(alphabet)):
        index_in_to_encoded = 0
        for char_to_encode in to_encode:
            if char_to_encode in alphabet[line_index]:
                encoded[index_in_to_encoded] = alphabet[line_index].index(char_to_encode) + 1, line_index + 1
                # print(char_to_encode, alphabet[line_index].index(char_to_encode), line_index) # буква, горизонталь, вертикаль
            index_in_to_encoded += 1

    # код чтобы посмотреть координаты в удобном формате
    # первая строка - горизонтальные координаты, а вторая - вертикальные
    # print()
    # horizontal = []
    # vertical = []
    # for element in encoded:
    #     horizontal.append(element[0])
    #     vertical.append(element[1])
    # print(horizontal)
    # print(vertical)
    # print()

    # а затем считываются построчно (получаем одномерный список)
    coords = []
    for element in encoded:
        if element:
            coords.append(element[0])
    for element in encoded:
        if element:
            coords.append(element[1])

    # сдвиг на нечётное кол-во шагов влево
    coords = coords[shift:] + coords[:shift]

    # разбивка получившегося списка на координаты (получаем список координат в виде кортежей)
    coords = [coords[i:i + 2] for i in range(0, len(coords), 2)]

    # считывание координат
    result = [""] * len(coords)
    index_of_char = 0
    for element in coords:
        result[index_of_char] = alphabet[element[1] - 1][element[0] - 1]
        index_of_char += 1

    return to_encode, "".join(result)


def first_decoding(to_decode):
    # определение алфавита
    alphabet = what_alphabet(to_encode)

    # шифровка (сдвиг символов сообщения на 1 линию вверх по алфавиту)
    decoded = [""] * len(to_decode)
    for line_index in range(len(alphabet)):
        line = alphabet[line_index]
        next_line = alphabet[(line_index - 1) % len(alphabet)]

        index_in_to_decoded = 0
        for char_to_decode in to_decode:
            if char_to_decode in line:
                # print("буква >>>", char_to_decode)  # буква
                decoded_char = next_line["".join(line).index(char_to_decode)]
                if decoded_char:
                    decoded[index_in_to_decoded] = decoded_char
                    # print("в букву >>>", decoded[index_in_to_decoded])  # в букву
                else:
                    decoded[index_in_to_decoded] = alphabet[(line_index - 2) % len(alphabet)][
                        "".join(line).index(char_to_decode)]
                    # print("в букву >>>", decoded[index_in_to_decoded])  # в букву
                # print()
            index_in_to_decoded += 1
    return to_decode, "".join(decoded)


def second_decoding(to_decode):
    # определение алфавита
    alphabet = what_alphabet(to_encode)

    # координаты записываются вертикально (получаем список координат в виде кортежей)
    decoded = [()] * len(to_decode)
    for line_index in range(len(alphabet)):
        index_in_to_decoded = 0
        for char_to_decode in to_decode:
            if char_to_decode in alphabet[line_index]:
                decoded[index_in_to_decoded] = alphabet[line_index].index(char_to_decode) + 1, line_index + 1
                # print(char_to_decode, alphabet[line_index].index(char_to_decode), line_index) # буква, горизонталь, вертикаль
            index_in_to_decoded += 1

    # дешифровка
    t = []
    [t.extend(i) for i in decoded]
    decoded = t
    horizontal = decoded[:len(decoded) // 2]
    vertical = decoded[len(decoded) // 2:]
    coords = list(zip(horizontal, vertical))

    # считывание координат
    result = [""] * len(coords)
    index_of_char = 0
    for element in coords:
        result[index_of_char] = alphabet[element[1] - 1][element[0] - 1]
        index_of_char += 1
    return to_decode, "".join(result)


def third_decoding(to_decode, shift=1):
    # определение алфавита
    alphabet = what_alphabet(to_encode)

    # координаты записываются вертикально (получаем список координат в виде кортежей)
    decoded = [()] * len(to_decode)
    for line_index in range(len(alphabet)):
        index_in_to_decoded = 0
        for char_to_decode in to_decode:
            if char_to_decode in alphabet[line_index]:
                decoded[index_in_to_decoded] = alphabet[line_index].index(char_to_decode) + 1, line_index + 1
                # print(char_to_decode, alphabet[line_index].index(char_to_decode), line_index) # буква, горизонталь, вертикаль
            index_in_to_decoded += 1

    # дешифровка
    t = []
    [t.extend(i) for i in decoded]
    decoded = t
    horizontal = decoded[:len(decoded) // 2]
    vertical = decoded[len(decoded) // 2:]

    coords = list(zip(horizontal, vertical))

    # тот самый сдвиг третьего метода
    coords = coords[-shift:] + coords[:-shift]
    coords[0] = (coords[0][1], coords[0][0])

    # считывание координат
    result = [""] * len(coords)
    index_of_char = 0
    for element in coords:
        result[index_of_char] = alphabet[element[1] - 1][element[0] - 1]
        index_of_char += 1
    return to_decode, "".join(result)


show_menu()
while True:
    inp = input("Итак, ваш выбор >>>").split()
    print()
    if inp[0] == "menu":
        show_menu()
    elif inp[0] == "exit":
        break
    elif inp[0] == "1":
        if inp[1] == "en":
            to_encode = input("Введите текст для зашифровки >>>")
            print()
            entered, result = first_encoding(to_encode)
            print("Введено >>>", entered)
            print("Получено >>>", result)
            print()
        elif inp[1] == "de":
            to_decode = input("Введите текст для дешифровки >>>")
            print()
            entered, result = first_decoding(to_decode)
            print("Введено >>>", entered)
            print("Получено >>>", result)
            print()
        else:
            print("Вы ввели что-то не то")
    elif inp[0] == "2":
        if inp[1] == "en":
            to_encode = input("Введите текст для зашифровки >>>")
            print()
            entered, result = second_encoding(to_encode)
            print("Введено >>>", entered)
            print("Получено >>>", result)
            print()
        elif inp[1] == "de":
            to_decode = input("Введите текст для дешифровки >>>")
            print()
            entered, result = second_decoding(to_decode)
            print("Введено >>>", entered)
            print("Получено >>>", result)
            print()
        else:
            print("Вы ввели что-то не то")
    elif inp[0] == "3":
        if inp[1] == "en":
            to_encode = input("Введите текст для зашифровки >>>")
            print()
            entered, result = third_encoding(to_encode)
            print("Введено >>>", entered)
            print("Получено >>>", result)
            print()
        elif inp[1] == "de":
            to_decode = input("Введите текст для дешифровки >>>")
            print()
            entered, result = third_decoding(to_decode)
            print("Введено >>>", entered)
            print("Получено >>>", result)
            print()
        else:
            print("Вы ввели что-то не то")
    else:
        print("Вы ввели что-то не то")
