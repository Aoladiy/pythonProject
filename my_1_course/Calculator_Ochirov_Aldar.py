from num2words import num2words

d = dict(ноль='0',
         один='1',
         два='2',
         три='3',
         четыре='4',
         пять='5',
         шесть='6',
         семь='7',
         восемь='8',
         девять='9',
         десять='10',
         одиннадцать='11',
         двенадцать='12',
         тринадцать='13',
         четырнадцать='14',
         пятнадцать='15',
         шестнадцать='16',
         семнадцать='17',
         восемнадцать='18',
         девятнадцать='19',
         двадцать='20',
         тридцать='30',
         сорок='40',
         пятьдесят='50',
         шестьдесят='60',
         семьдесят='70',
         восемьдесят='80',
         девяносто='90',
         сто='100',
         двести='200',
         триста='300',
         четыреста='400',
         пятьсот='500',
         шестьсот='600',
         семьсот='700',
         восемьсот='800',
         девятьсот='900',
         тысяча='1000',
         миллион='1000000',
         миллиард='1000000000',
         и='.',
         )
d1 = ['20',
      '30',
      '40',
      '50',
      '60',
      '70',
      '80',
      '90'
      ]
d2 = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9'
]


def calculator(inp):
    if 'плюс' in inp:
        s = inp.split('плюс')
        s1 = s[0]
        s2 = s[1]
        su = 0
        su1 = ''
        su2 = ''
        su3 = ''
        su4 = ''
        su5 = ''
        su6 = ''
        su7 = ''
        su8 = ''
        if len(s1.split()) == 1:
            s1 = s1.split()
            su1 = d[s1[0]]
        elif len(s1.split()) > 1:
            s1 = s1.split()
            su2 = d[s1[0]]
            su3 = d[s1[1]]
            su4 = su2 + su3
        if len(s2.split()) == 1:
            s2 = s2.split()
            su5 = d[s2[0]]
        elif len(s1.split()) > 1:
            s2 = s2.split()
            su6 = d[s2[0]]
            su7 = d[s2[1]]
            su8 = su6 + su7
        print(su1, su4, su5, su8)
        su = eval(su1, '+', su4, '+', su5, '+', su8)
        print(num2words(su, lang='ru'))
    if 'минус' in inp:
        s = inp.split('минус')
        s1 = s[0].split()
        s2 = s[1].split()
        diff = 0
        diff1 = ''
        diff2 = ''
        for i in range(len(s1)):
            diff1 += d[s1[i]]
        for i in range(len(s2)):
            diff2 += d[s2[i]]
        diff = eval(diff1 + '-' + diff2)
        print(num2words(diff, lang='ru'))
    if 'умножить на' in inp:
        s = inp.split('умножить на')
        s1 = s[0].split()
        s2 = s[1].split()
        multy = 0
        multy1 = ''
        multy2 = ''
        for i in range(len(s1)):
            multy1 += d[s1[i]]
        for i in range(len(s2)):
            multy2 += d[s2[i]]
        multy = eval(multy1 + '*' + multy2)
        print('Ответ:', num2words(multy, lang='ru'))
    if 'делить на' in inp:
        s = inp.split('делить на')
        s1 = s[0].split()
        s2 = s[1].split()
        quo = 0
        quo1 = ''
        quo2 = ''
        for i in range(len(s1)):
            quo1 += d[s1[i]]
            print(quo1)
        for i in range(len(s2)):
            quo2 += d[s2[i]]
            print(quo2)
        quo = eval(quo1 + '/' + quo2)
        print('Ответ:', num2words(quo, lang='ru'))


calculator(input('введите выражение: '))
