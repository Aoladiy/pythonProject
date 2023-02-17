import random

import numpy as np

# First task
print('Первое задание')
a = np.loadtxt('../../data/minutes_n_ingredients.csv', dtype='int32', skiprows=1, delimiter=',')
print('Первые пять строк массива', a[:5], sep='\n')
print()

# Second task
print('Второе задание')
print(f'Среднее значение по второму столбцу >>> {np.average(a[:, 1])}',
      f'Среднее значение по третьему столбцу >>> {np.average(a[:, 2])}', sep='\n')
print(f'Минимальное значение по второму столбцу >>> {np.min(a[:, 1])}',
      f'Минимальное значение по третьему столбцу >>> {np.min(a[:, 2])}', sep='\n')
print(f'Максимальное значение по второму столбцу >>> {np.max(a[:, 1])}',
      f'Максимальное значение по третьему столбцу >>> {np.max(a[:, 2])}', sep='\n')
print(f'Медиана по второму столбцу >>> {np.median(a[:, 1])}',
      f'Медиана по третьему столбцу >>> {np.median(a[:, 2])}', sep='\n')
print()

# Third task
print('Третье задание')
q0_75 = int(np.quantile(a[:, 1], 0.75))  # q0_75 == 65
print(np.where(a[:, 1] >= q0_75, q0_75, a[:, 1]))
print()

# Fourth task
print('Четвёртое задание')
print(f'Кол-во нулей >>> {np.count_nonzero(np.where(a[:, 1] != 0, 0, 1))}')
# изменяем время с нулей на единицы
b = np.where(a[:, 1] == 0, 1, a[:, 1])
print()

# Fifth task
print('Пятое задание')
print(f'Кол-во уникальных рецептов >>> {np.size(a[:, 0])}')
print()

# sixth task
print('Шестое задание')
values, counts = np.unique(a[:, 2], return_counts=True)
print('Уникальные значения и их частота соответственно', *zip(values, counts), sep='\n')
print()

# seventh task
print('Седьмое задание')
print(a[np.where(a[:, 2] <= 5)])
print()

# eights task
print('Восьмое задание')
test = a[np.where(a[:, 1] != 0)]
print(np.where(True, test[:, 2] / test[:, 1], 0))
print(np.max(np.where(True, test[:, 2] / test[:, 1], 0)))
print()

# ninths task
print('Девятое задание')
print(np.average(a[np.where(np.sort(a[:, 1])[-100:])][:, 2]))
print()

# tenth task
print('Десятое задание')
print(a[np.random.randint(np.size(a[:, 0]), size=10)])
print()

# eleventh task
print('Одиннадцатое задание')
print((np.size(np.where(a[:, 2] < np.average(a[:, 2]))) / np.size(a[:, 2]) * 100))
print()

# twelfth task
print('Двенадцатое задание')
print(np.column_stack((a, np.where((a[:, 1] <= 20) & (a[:, 2] <= 5), 1, 0))))
print()

# therteenth task
print('Тринадцатое задание')
print(f'Процент "простых" рецептов в датасете:',
      np.sum(np.column_stack((a, np.where((a[:, 1] <= 20) & (a[:, 2] <= 5), 1, 0)))[:, 3]) / 100000 * 100)
print()

# fourteen task
print('Четырнадцатое задание')
print(*np.array([a[np.where(a[:, 1] <= 10)], a[np.where((a[:, 1] > 10) & (a[:, 1] < 20))], a[np.where(a[:, 1] >= 20)]],
                dtype=object))
