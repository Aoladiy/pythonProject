import numpy


def complex_calculator():
    print(
        '''Режим 0 - калькулятор(+-/*),
режим 1 - перевод числа в тригонометрическую форму,
режим 2 - возведение в степень или в корень''')
    print('Пример ввода элемента 5+15j')
    mode = input('Введите номер режима (0, 1 или 2): ')

    if mode == '0':
        a = complex(input('Первое число: '))
        b = complex(input('Второе число: '))
        c = input('Какое действие необходимо: + или - или / или *: ')
        if c == '+':
            print('Ответ:', a + b)
        elif c == '-':
            print('Ответ:', a - b)
        elif c == '*':
            print('Ответ:', a * b)
        elif c == '/' and b != 0:
            print('Ответ:', a / b)
        else:
            print('На ноль делить нельзя! ')

    if mode == '1':
        a = complex(input('Введите число: '))
        fi = numpy.arctan(a.imag / a.real)
        r = (a.imag ** 2 + a.real ** 2) ** 0.5
        print('Ответ:', 'z = ', r, '(cos(', fi, ') + i*sin(', fi, ')')

    if mode == '2':
        b = input('Возвести в степень или в корень: ')
        if b == 'степень':
            a = complex(input('число: '))
            n = int(input('степень: '))
            print('Ответ ', a ** n)
        elif b == 'корень':
            a = complex(input('число: '))
            n = int(input('корень какой степени?: '))
            if n != 0:
                n = 1 / n
                print('Ответ ', a ** n)
            else:
                print('Ответ ', 1)


while True:
    complex_calculator()
