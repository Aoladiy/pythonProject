import pandas as pd

k = 3
ni = 3
i = (1, 2, 3)
n = 9
count = int(input('Сколько чисел вы хотите видеть в выборках? >>> '))
x1 = (int(input('Первое число первой выборки >>> ')), int(input('Второе число первой выборки >>> ')),
      int(input('Третье число первой выборки >>> ')))
x2 = (int(input('Первое число второй выборки >>> ')), int(input('Второе число второй выборки >>> ')),
      int(input('Третье число второй выборки >>> ')))
x3 = (int(input('Первое число третей выборки >>> ')), int(input('Второе число третей выборки >>> ')),
      int(input('Третье число третей выборки >>> ')))

# нужно найти межгрупповую дисперсию δ2 и среднюю групповую дисперсию σ2


# Средние значения внутри групп
avg_x1 = sum(x1) / len(x1)
avg_x2 = sum(x2) / len(x2)
avg_x3 = sum(x3) / len(x3)

# выборочное среднее равно
avg_x = (ni * avg_x1 + ni * avg_x2 + ni * avg_x3) / 9

# Выборочные дисперсии внутри групп
d1_sqrt = ((x1[0] - avg_x1) ** 2 + (x1[1] - avg_x1) ** 2 + (x1[2] - avg_x1) ** 2) / ni
d2_sqrt = ((x2[0] - avg_x2) ** 2 + (x2[1] - avg_x2) ** 2 + (x2[2] - avg_x2) ** 2) / ni
d3_sqrt = ((x3[0] - avg_x3) ** 2 + (x3[1] - avg_x3) ** 2 + (x3[2] - avg_x3) ** 2) / ni

# средняя групповая дисперсия
q1 = (ni * d1_sqrt + ni * d2_sqrt + ni * d3_sqrt) / n

# межгрупповая дисперсия
q = ((avg_x1 - avg_x) ** 2 * ni + (avg_x2 - avg_x) ** 2 * ni + (avg_x3 - avg_x) ** 2 * ni) / n

# Вычислим теперь наблюдаемое значение статистики Фишера F
# и завершим проверку гипотезы H0

F = ((1 / (k - 1)) * q) / ((1 / (n - k)) * q1)
print('F >>>', F)

# Фишер
with open('fisher.txt', encoding='utf-8') as fish:
    all_id = []
    lines = []
    for line in fish:
        line = list(map(lambda x: float(x.replace(',', '.')), line.split()))
        all_id.append(int(line[0]))
        lines.append(line[1:])
    fisher = pd.DataFrame(data=lines, index=all_id, columns=[i for i in range(1, 11)])

F1 = fisher[k - 1][n - k]
print('F1 >>>', F1)

if F > F1:
    print('Отвергается')
else:
    print('Подтверждается')
