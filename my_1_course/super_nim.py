import sys
import random

print('Нужно рассказать правила? (да или что-угодно): ')
f_yes_or_no = input()
if f_yes_or_no == "да":
    print('''На шахматной доске в некоторых клетках случайно разбросаны фишки или пуговицы.
Где стоит цифра 1 фишка есть, где 0 - фишки нет
Игроки ходят по очереди.
За один ход можно снять все фишки с какой-либо горизонтали или вертикали, на которой они есть.
Выигрывает тот, кто заберет последние фишки.
Вводите одно значение от a до h (латиница) чтобы убрать все фишки по вертикали
или от 1 до 8 чтобы убрать все фишки по горизонтали''')

yes_or_no = input('введите "да" чтобы продолжить и "нет" чтобы выйти: ')
while yes_or_no != 'да' or yes_or_no != 'нет':
    if yes_or_no == 'да':
        print()
        print('Продолжаем...')
        break
    elif yes_or_no == 'нет':
        print()
        sys.exit('Выходим...')
    yes_or_no = input('я не понимаю, попробуй снова: ')
print()
print('А вот и доска')
print()

desk = list([[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]
             ])
temp = 0
for i in range(8):
    for j in range(8):
        temp = random.randrange(0, 2)
        desk[i].insert(j, temp)
        print(desk[i][j], end='   ')
    print()

step = 1
f_p = 0
s_p = 0
bl = True
while bl:
    while step % 2 != 0:
        f_p = input('ход первого игрока: ')
        if f_p == 'a':
            for i in range(8):
                for j in range(8):
                    desk[i][0] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        elif f_p == 'b':
            for i in range(8):
                for j in range(8):
                    desk[i][1] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        elif f_p == 'c':
            for i in range(8):
                for j in range(8):
                    desk[i][2] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        elif f_p == 'd':
            for i in range(8):
                for j in range(8):
                    desk[i][3] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        elif f_p == 'e':
            for i in range(8):
                for j in range(8):
                    desk[i][4] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        elif f_p == 'f':
            for i in range(8):
                for j in range(8):
                    desk[i][5] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        elif f_p == 'g':
            for i in range(8):
                for j in range(8):
                    desk[i][6] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        elif f_p == 'h':
            for i in range(8):
                for j in range(8):
                    desk[i][7] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        elif f_p == '1':
            for i in range(8):
                for j in range(8):
                    desk[0][j] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        elif f_p == '2':
            for i in range(8):
                for j in range(8):
                    desk[1][j] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        elif f_p == '3':
            for i in range(8):
                for j in range(8):
                    desk[2][j] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        elif f_p == '4':
            for i in range(8):
                for j in range(8):
                    desk[3][j] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        elif f_p == '5':
            for i in range(8):
                for j in range(8):
                    desk[4][j] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        elif f_p == '6':
            for i in range(8):
                for j in range(8):
                    desk[5][j] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        elif f_p == '7':
            for i in range(8):
                for j in range(8):
                    desk[6][j] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        elif f_p == '8':
            for i in range(8):
                for j in range(8):
                    desk[7][j] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        else:
            print('неверное значение')
    if desk == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]:
        if step % 2 != 0:
            print('победил второй игрок!')
            bl = False
            break
        else:
            print('победил первый игрок!')
            bl = False
            break
    while step % 2 == 0:
        s_p = input('ход второго игрока: ')
        if s_p == 'a':
            for i in range(8):
                for j in range(8):
                    desk[i][0] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        elif s_p == 'b':
            for i in range(8):
                for j in range(8):
                    desk[i][1] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        elif s_p == 'c':
            for i in range(8):
                for j in range(8):
                    desk[i][2] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        elif s_p == 'd':
            for i in range(8):
                for j in range(8):
                    desk[i][3] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        elif s_p == 'e':
            for i in range(8):
                for j in range(8):
                    desk[i][4] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        elif s_p == 'f':
            for i in range(8):
                for j in range(8):
                    desk[i][5] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        elif s_p == 'g':
            for i in range(8):
                for j in range(8):
                    desk[i][6] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        elif s_p == 'h':
            for i in range(8):
                for j in range(8):
                    desk[i][7] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        elif s_p == '1':
            for i in range(8):
                for j in range(8):
                    desk[0][j] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        elif s_p == '2':
            for i in range(8):
                for j in range(8):
                    desk[1][j] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        elif s_p == '3':
            for i in range(8):
                for j in range(8):
                    desk[2][j] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        elif s_p == '4':
            for i in range(8):
                for j in range(8):
                    desk[3][j] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        elif s_p == '5':
            for i in range(8):
                for j in range(8):
                    desk[4][j] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        elif s_p == '6':
            for i in range(8):
                for j in range(8):
                    desk[5][j] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        elif s_p == '7':
            for i in range(8):
                for j in range(8):
                    desk[6][j] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        elif s_p == '8':
            for i in range(8):
                for j in range(8):
                    desk[7][j] = 0
                    print(desk[i][j], end='   ')
                print()
            step += 1
        else:
            print('неверное значение')
    if desk == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]:
        if step % 2 != 0:
            print('победил второй игрок!')
            bl = False
            break
        else:
            print('победил первый игрок!')
            bl = False
            break
