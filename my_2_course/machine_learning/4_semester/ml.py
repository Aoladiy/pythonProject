import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("../../data/ml_data.csv")

# task 1
# a = np.array([i for i in range(1, 11)])
# b = np.array([i for i in range(1, 11)])
#
# table = a[:, np.newaxis] * b[np.newaxis, :]
# print(table)

# task 2
# def create_arithmetic_matrix(N, a, d):
#     arr = np.array([a + i * d for i in range(N)])
#     return np.diag(arr)
#
# # Пример использования функции
# result = create_arithmetic_matrix(5, 1, 2)
# print(result)

# task 3
# A = np.arange(1, 26).reshape(5, 5)
# odd_elements = A[::2, ::2].flatten()
# print(odd_elements)

# task 4
# # создаем пустой массив
# arr = np.zeros((5, 5), dtype=int)
#
# # заполняем границы единицами
# arr[0, :] = 1
# arr[-1, :] = 1
# arr[:, 0] = 1
# arr[:, -1] = 1
#
# # выводим массив
# print(arr)

# task 5
# # Создаем массив (2,2) содержащий 5 и 0
# a = np.array([[5, 0], [0, 5]])
#
# # Повторяем его в шахматном порядке для создания матрицы (5,5)
# A = np.tile(a, (3, 3))
#
# # Создаем нулевую матрицу размером (5,5)
# B = np.zeros((5, 5))
#
# # Заполняем диагональные элементы 5
# np.fill_diagonal(B, 5)
#
# # Извлекаем нижнюю треугольную матрицу
# B = np.tril(B)
# # Вычисляем детерминанты матриц
# det_A = np.linalg.det(A)
# det_B = np.linalg.det(B)
#
# # Находим обратные матрицы
# inv_A = np.linalg.inv(A)
# inv_B = np.linalg.inv(B)
#
# print("Матрица A:\n", A)
# print("Детерминант матрицы A:", det_A)
# print("Обратная матрица A:\n", inv_A)
#
# print("Матрица B:\n", B)
# print("Детерминант матрицы B:", det_B)
# print("Обратная матрица B:\n", inv_B)

# task 6
# data = pd.read_csv("../../data/ml_data.csv")

# task 7
# # вывод первых 5 строк
# print(data.head())
#
# # вывод последних 5 строк
# print(data.tail())

# task 8
# # вывод информации о датасете
# print(data.info())
#
# # вывод статистических параметров численных полей
# print(data.describe())

# task 9
# data.drop(columns=["Ecology_1", "Ecology_2",
#                    "Ecology_3", "Social_1", "Social_2", "Social_3", "Healthcare_1",
#                    "Helthcare_2", "Shops_1", "Shops_2"], inplace=True)
# data.rename(columns={
#     "Id": "Идентификатор", "DistrictId": "ИдентификаторОбласти", "Rooms": "Комнаты", "Square": "Площадь",
#     "LifeSquare": "ЖилаяПлощадь", "KitchenSquare": "ПлощадьКухни",
#     "Floor": "Пол", "HouseFloor": "Этаж", "HouseYear": "ЛетДому", "Price": "Цена"
# }, inplace=True)
# print(data.columns)

# task 10
# # Вывод отдельно столбца "Цена" по номеру и названию
# print(data.iloc[:, 9])
# print(data['Цена'])
#
# # Вывод первой, десятой и предпоследней строки по номеру
# print(data.iloc[[0, 9, 9998]])
#
# # Вывод первой, десятой и предпоследней строки по индексу
# print(data.loc[[0, 9, 9998]])

# task 11
# # выделение последних десяти строк в отдельную таблицу
# last_10 = data.tail(10)
#
# # удаление столбца с ценой из последней таблицы
# last_10 = last_10.drop('Цена', axis=1)
#
# # склеивание таблиц
# merged_data = data.append(last_10)
#
# # заполнение отсутствующих значений цены средним по таблице
# mean_price = merged_data['Цена'].mean()
# merged_data['Цена'] = merged_data['Цена'].fillna(mean_price)
#
# # вывод первых строк таблицы
# print(merged_data.head())

# task 12
# # выделяем пять последних колонок в отдельную таблицу
# last_five_cols = data.iloc[:, -5:]
#
# # удаляем строки с ценами ниже среднего
# avg_price = data['Цена'].mean()
# last_five_cols = last_five_cols[last_five_cols['Цена'] >= avg_price]
#
# # присоединяем таблицы
# result = pd.concat([data, last_five_cols], axis=1)

# task 13
# # Группировка данных по этажу
# grouped = data.groupby("Этаж")
#
# # Расчет средней цены и количества квартир на каждом этаже
# result = grouped.agg({"Цена": "mean", "Идентификатор": "count"})
#
# # Вывод результатов
# print(result)

# task 14
# # сохранение в формате csv
# data.to_csv('../../data/data_task_14.csv', index=False)
#
# # сохранение в формате xlsx
# data.to_excel('../../data/data_task_14.xlsx', index=False)
#
# # чтение из файла csv
# df_csv = pd.read_csv('../../data/data_task_14.csv')
#
# # чтение из файла xlsx
# df_xlsx = pd.read_excel('../../data/data_task_14.xlsx')
#
# # вывод на экран
# print('Table from CSV:')
# print(df_csv)
#
# print('Table from XLSX:')
# print(df_xlsx)

# task 15
# table = pd.read_excel('../../data/ml_task_15.xlsx')
# print(table)

# task 16

# task 17
# # Рассчитаем количество квартир для каждого числа комнат
# room_counts = data['Rooms'].value_counts()
#
# # Создадим круговую диаграмму
# fig, ax = plt.subplots(figsize=(6, 6))
#
# # Найдем сектор с максимальным количеством квартир и выдвинем его
# max_room_count = room_counts.max()
# max_room_index = room_counts.idxmax()
# explode = [0] * len(room_counts)
# explode[room_counts.index.get_loc(max_room_index)] = 0.1
#
# ax.pie(room_counts, labels=room_counts.index, autopct='%1.1f%%', startangle=90, explode=explode)
#
# plt.title('Количество квартир в зависимости от количества комнат')
# plt.show()

# task 18
# # Построение гистограммы
# plt.hist(data['Price'], bins=100)
#
# # Настройка графика
# plt.title('Распределение цен на квартиры')
# plt.xlabel('Цена')
# plt.ylabel('Количество квартир')
#
# # Отображение графика
# plt.show()

# task 19
# fig, axs = plt.subplots(2, 2, figsize=(10, 10))
#
# axs[0, 0].scatter(data['Rooms'], data['Price'])
# axs[0, 0].set_xlabel('Rooms')
# axs[0, 0].set_ylabel('Price')
#
# axs[0, 1].scatter(data['Square'], data['Price'])
# axs[0, 1].set_xlabel('Square')
# axs[0, 1].set_ylabel('Price')
#
# axs[1, 0].scatter(data['HouseFloor'], data['Price'])
# axs[1, 0].set_xlabel('HouseFloor')
# axs[1, 0].set_ylabel('Price')
#
# axs[1, 1].scatter(data['HouseYear'], data['Price'])
# axs[1, 1].set_xlabel('HouseYear')
# axs[1, 1].set_ylabel('Price')
#
# plt.show()

# task 20
# # Ядерная оценка плотности целевой переменной Price
# sns.kdeplot(data['Price'])
# plt.title('Ядерная оценка плотности для переменной Price')
#
# # Двумерная ядерная оценка плотности для переменной Price и признака HouseFloor
# sns.kdeplot(data=data, x='HouseFloor', y='Price', cmap="Blues", shade=True, shade_lowest=False)
# plt.title('Двумерная ядерная оценка плотности для переменной Price и признака HouseFloor')
#
# # Точечная диаграмма для переменных Price и HouseFloor
# plt.scatter(data['HouseFloor'], data['Price'], s=10, alpha=0.5, c='b')
# plt.title('Зависимость переменной Price от признака HouseFloor')
# plt.xlabel('HouseFloor')
# plt.ylabel('Price')
#
# plt.show()

# task 21
# # Определяем данные для построения ящиковой диаграммы
# data_to_plot = [data['Square'].dropna()]
#
# # Строим ящиковую диаграмму
# fig, ax = plt.subplots(figsize=(6, 6))
# ax.boxplot(data_to_plot, vert=False, widths=0.7)
#
# # Определяем границы усов ящика
# q1, q3 = data['Square'].quantile([0.25, 0.75])
# iqr = q3 - q1
# whisker_width = 1.5
# lower_whisker = q1 - whisker_width * iqr
# upper_whisker = q3 + whisker_width * iqr
#
# # Определяем границы выбросов
# outliers = data['Square'][(data['Square'] < lower_whisker) | (data['Square'] > upper_whisker)]
# lower_outlier = outliers.min()
# upper_outlier = outliers.max()
#
# # Выводим границы усов и выбросов на диаграмму
# ax.axvline(lower_whisker, color='gray', linestyle='--', linewidth=1)
# ax.axvline(upper_whisker, color='gray', linestyle='--', linewidth=1)
# ax.axvline(lower_outlier, color='red', linestyle='--', linewidth=1)
# ax.axvline(upper_outlier, color='red', linestyle='--', linewidth=1)
#
# # Выводим диаграмму
# plt.title('Ящиковая диаграмма признака Square')
# plt.show()

# task 22
# # выбираем нужные признаки из DataFrame
# features = ['Rooms', 'Square', 'HouseFloor', 'HouseYear', 'Price']
# data_subset = data[features]
#
# # создаем сетку графиков
# g = sns.PairGrid(data_subset)
# g.map_diag(sns.histplot)
# g.map_lower(sns.kdeplot)
# g.map_upper(sns.scatterplot)

# task 23
# # создаем матрицу корреляции
# corr_matrix = data[['Rooms', 'Square', 'HouseFloor', 'HouseYear', 'Price']].corr()
#
# # строим тепловую карту
# sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
#
# # выводим график на экран
# plt.show()