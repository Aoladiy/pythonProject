import numpy as np
from numpy import linalg as la


n = int(input('Размерность матрицы: '))
print('''Вводите элементы матрицы через пробел,
 а чтобы начать новую строку нажмите пробел''')
A = [[int(j) for j in input('Вводите элементы: ').split()] for i in range(n)]
A_inv = np.linalg.inv(A)
print('Обратная матрица: ', A_inv)
print('Ранг матрицы: ', la.matrix_rank(A))
