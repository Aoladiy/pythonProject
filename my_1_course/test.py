field = []
for _ in range(40):
    t = ['.' for _ in range(40)]
    field.append(t)


def print_():
    #                         а это нумерация поля от 0 до 39 по вертикальной оси
    # for i in range(len(field)):
    #     if i < 30:
    #         field[i].insert(0, str(39 - i))
    #     else:
    #         field[i].insert(0, str(39 - i) + ' ')

    for i in range(len(field)):
        print(*field[i])


class Line:
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    def draw(self):
        x1 = self.x1
        y1 = self.y1
        x2 = self.x2
        y2 = self.y2

        dx = x2 - x1
        dy = y2 - y1

        sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
        sign_y = 1 if dy > 0 else -1 if dy < 0 else 0

        if dx < 0: dx = -dx
        if dy < 0: dy = -dy

        if dx > dy:
            pdx, pdy = sign_x, 0
            es, el = dy, dx
        else:
            pdx, pdy = 0, sign_y
            es, el = dx, dy

        x, y = x1, y1

        error, t = el / 2, 0

        field[y][x] = '*'

        while t < el:
            error -= es
            if error < 0:
                error += el
                x += sign_x
                y += sign_y
            else:
                x += pdx
                y += pdy
            t += 1
            field[y][x] = '*'


class Figure:
    x = 0
    y = 0
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    def draw(self):
        field[self.y][self.x] = '*'
        field[self.y1][self.x1] = '*'


class Rectangle(Figure):
    def draw(self):
        for i in range(min(self.y, self.y1), max(self.y, self.y1) + 1):
            field[i][self.x] = '*'
        for i in range(min(self.y, self.y1), max(self.y, self.y1) + 1):
            field[i][self.x1] = '*'
        for i in range(min(self.x, self.x1), max(self.x, self.x1) + 1):
            field[self.y][i] = '*'
        for i in range(min(self.x, self.x1), max(self.x, self.x1) + 1):
            field[self.y1][i] = '*'

    def area(self):
        if round((max(-self.y - 1, -self.y1 - 1) - min(-self.y - 1, -self.y1 - 1) + 1) * (
                max(self.x, self.x1) - min(self.x, self.x1) + 1), 4) == 1:
            return 'площадь прямоугольника:', 0.0
        else:
            return 'площадь прямоугольника:', round(
                (max(-self.y - 1, -self.y1 - 1) - min(-self.y - 1, -self.y1 - 1) + 1) * (
                        max(self.x, self.x1) - min(self.x, self.x1) + 1), 4)


class Triangle(Figure):
    def draw(self):
        flag = True
        x = self.x
        y = self.y
        x1 = self.x1
        y1 = self.y1
        x2 = self.x2
        y2 = self.y2
        #                  остатки старого кода, возможно неправильного, может ещё пригодятся... когда-нибудь...
        # f_length = ((x1 - x) ** 2 + (y1 - y) ** 2) ** 0.5
        # s_length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        # t_length = ((x2 - x) ** 2 + (y2 - y) ** 2) ** 0.5
        # if f_length + s_length > t_length and f_length + t_length > s_length and s_length + t_length > f_length:
        #     pass
        # else:
        #     print('Такой треугольник не существует')
        #     flag = False
        # if flag:
        y = -self.y - 1
        y1 = -self.y1 - 1
        y2 = -self.y2 - 1
        first_line, second_line, third_line = Line(), Line(), Line()
        first_line.x1 = x
        first_line.y1 = y
        first_line.x2 = x1
        first_line.y2 = y1
        second_line.x1 = x1
        second_line.y1 = y1
        second_line.x2 = x2
        second_line.y2 = y2
        third_line.x1 = x
        third_line.y1 = y
        third_line.x2 = x2
        third_line.y2 = y2
        for i in [first_line, second_line, third_line]:
            i.draw()

    def area(self):
        x = self.x
        y = self.y
        x1 = self.x1
        y1 = self.y1
        x2 = self.x2
        y2 = self.y2

        f_length = ((x1 - x) ** 2 + (y1 - y) ** 2) ** 0.5
        s_length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        t_length = ((x2 - x) ** 2 + (y2 - y) ** 2) ** 0.5
        p = (f_length + s_length + t_length) / 2
        return 'площадь треугольника:', round((p * (p - f_length) * (p - s_length) * (p - t_length)) ** 0.5, 4)


class Square(Figure):
    def draw(self):
        flag = True
        if (max(self.x, self.x1) - min(self.x, self.x1)) != (max(self.y, self.y1) - min(self.y, self.y1)):
            print('Это не квадрат!')
            flag = False
        if flag:
            for i in range(min(self.y, self.y1), max(self.y, self.y1) + 1):
                field[i][self.x] = '*'
            for i in range(min(self.y, self.y1), max(self.y, self.y1) + 1):
                field[i][self.x1] = '*'
            for i in range(min(self.x, self.x1), max(self.x, self.x1) + 1):
                field[self.y][i] = '*'
            for i in range(min(self.x, self.x1), max(self.x, self.x1) + 1):
                field[self.y1][i] = '*'

    def area(self):
        if round((max(-self.y - 1, -self.y1 - 1) - min(-self.y - 1, -self.y1 - 1) + 1) * (
                max(self.x, self.x1) - min(self.x, self.x1) + 1), 4) == 1:
            return 'площадь квадрата:', 0.0
        else:
            return 'площадь квадрата:', round((max(-self.y - 1, -self.y1 - 1) - min(-self.y - 1, -self.y1 - 1) + 1) * (
                    max(self.x, self.x1) - min(self.x, self.x1) + 1), 4)


class Rhombus(Figure):
    def draw(self):
        flag = True
        x = self.x
        y = -self.y - 1
        x1 = self.x
        y1 = -self.y1 - 1
        x2 = self.x2
        x31 = (max(self.x, self.x2) - min(self.x, self.x2)) + self.x
        x32 = abs((max(self.x, self.x2) - min(self.x, self.x2)) - self.x)
        y3 = -int((max(self.y, self.y1) - min(self.y, self.y1)) / 2 + min(self.y, self.y1)) - 1
        vertical, horizontal = Line(), Line()
        north_west, north_east, south_east, south_west = Line(), Line(), Line(), Line()
        if (max(self.y, self.y1) - min(self.y, self.y1)) % 2 == 1:
            print('При таких координатах ромб не получится')
            flag = False
        if flag:
            try:
                vertical.x1 = x
                vertical.x2 = x1
                vertical.y1 = y
                vertical.y2 = y1
                # можно раскоментировать и получить вертикальную диагональ
                # vertical.draw()
                horizontal.x1 = x31
                horizontal.x2 = x32
                horizontal.y1 = y3
                horizontal.y2 = y3
                # можно раскоментировать и получить горизонтальную диагональ
                # horizontal.draw()
                north_west.x1 = x
                north_west.x2 = x32
                north_west.y1 = y1
                north_west.y2 = y3
                north_west.draw()
                north_east.x1 = x
                north_east.x2 = x31
                north_east.y1 = y1
                north_east.y2 = y3
                north_east.draw()
                south_west.x1 = x
                south_west.x2 = x32
                south_west.y1 = y
                south_west.y2 = y3
                south_west.draw()
                south_east.x1 = x
                south_east.x2 = x31
                south_east.y1 = y
                south_east.y2 = y3
                south_east.draw()
            except IndexError:
                print('Фигура не вмещается в поле')

    def area(self):
        x = self.x
        y = -self.y - 1
        x1 = self.x
        y1 = -self.y1 - 1
        x2 = self.x2
        x31 = (max(self.x, self.x2) - min(self.x, self.x2)) + self.x
        x32 = abs((max(self.x, self.x2) - min(self.x, self.x2)) - self.x)
        y3 = -int((max(self.y, self.y1) - min(self.y, self.y1)) / 2 + min(self.y, self.y1)) - 1
        vertical = ((y - y1) ** 2 + (x - x1) ** 2) ** 0.5 + 1
        horizontal = ((y3 - y3) ** 2 + (x31 - x32) ** 2) ** 0.5 + 1
        if round((vertical * horizontal) / 2, 4) == 0.5:
            return 'площадь ромба:', 0.0
        else:
            return 'площадь ромба:', round((vertical * horizontal) / 2, 4)


# f = Rectangle()
# f.x = 5
# f.y = -5 - 1
# f.x1 = 30
# f.y1 = -30 - 1
# # f.draw()
# f1 = Triangle()
# f1.x = 38
# f1.y = 12
# f1.x1 = 27
# f1.y1 = 39
# f1.x2 = 38
# f1.y2 = 37
# # f1.draw()
# f2 = Square()
# f2.x = 18
# f2.y = -7 - 1
# f2.y1 = -2 - 1
# f2.x1 = 13
# # f2.draw()
# f3 = Rhombus()
# # x2 - крайний x, x - x, через который будет проходить вертикальная диагональ, а игрики: крайний нижний и крайний верхний
# f3.x = 20
# f3.x2 = 10
# f3.y = 4
# f3.y1 = 26
# # f3.draw()
# l = Line()
# l.x1, l.y1, l.x2, l.y2 = 34, 33, 1, 15
# # l.draw()


# There will be menu
while True:
    f = Rectangle()
    f1 = Triangle()
    f2 = Square()
    f3 = Rhombus()
    l = Line()
    print('''1 - прямоугольник, 2 - треугольник, 3 - квадрат,
4 - ромб, 5 - линия, 0 - чтобы остановиться и вывести поле.
>>>Стоит принять во внимание, что отсчёт ведётся с 0 включительно!!!<<<''')
    first_ask = input('>>> ')
    if first_ask == '1':
        print('по двум противоположным диагональным точкам')
        f = Rectangle()
        f.x = int(input('x первой точки: '))
        f.y = -int(input('y первой точки: ')) - 1
        f.x1 = int(input('x второй точки: '))
        f.y1 = -int(input('y второй точки: ')) - 1
        f.draw()
    if first_ask == '2':
        print('по трём точкам')
        f = Triangle()
        f1.x = int(input('x первой точки: '))
        f1.y = int(input('y первой точки: '))
        f1.x1 = int(input('x второй точки: '))
        f1.y1 = int(input('y второй точки: '))
        f1.x2 = int(input('x третьей точки: '))
        f1.y2 = int(input('y третьей точки: '))
        f1.draw()
    if first_ask == '3':
        print('по двум противоположным диагональным точкам')
        f2 = Square()
        f2.x = int(input('x первой точки: '))
        f2.y = -int(input('y первой точки: ')) - 1
        f2.x1 = int(input('x второй точки: '))
        f2.y1 = -int(input('y второй точки: ')) - 1
        f2.draw()
    if first_ask == '4':
        print('''x2 - крайний x, x - x, через который будет проходить вертикальная диагональ,
а игрики: крайний нижний и крайний верхний''')
        f3.x = int(input('x: '))
        f3.x2 = int(input('x2: '))
        f3.y = int(input('y: '))
        f3.y1 = int(input('y1: '))
        f3.draw()
    if first_ask == '5':
        print('по двум точкам')
        l = Line()
        l.x1 = int(input('x первой точки: '))
        l.y1 = -int(input('y первой точки: ')) - 1
        l.x2 = int(input('x второй точки: '))
        l.y2 = -int(input('y второй точки: ')) - 1
        l.draw()
    if first_ask == '0':
        print_()
        break
    sum_s = 0
    for i in [f, f1, f2, f3, l]:
        try:
            sum_s += i.area()[1]
            print(*i.area())
        except AttributeError:
            pass
    print('сумма площадей:', sum_s)
# print_()
