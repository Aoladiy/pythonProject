import re

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1 Загрузите данные по вариантам в ноутбук.
# загружаем данные из Excel файла
df = pd.read_excel('../../data/ml/Вариант 1.xlsx', skiprows=2, skipfooter=1)

# 2 Сделайте описательную статистику полученных данных.
# получаем описательную статистику для всех количественных столбцов
desc_stats = df.describe()
print(desc_stats)

# 3 Найдите процент учащихся, выполнивших работу ниже среднего.
# вычисляем среднее значение для столбца "Балл"
mean_score = df['Балл'].mean()

# отфильтровываем строки с баллом ниже среднего
filtered_df = df[df['Балл'] < mean_score]

# вычисляем процент отфильтрованных строк
percentage = len(filtered_df) / len(df) * 100

print(f"Процент учащихся с баллом ниже среднего: {percentage:.2f}%")

# 4 Найти процент учащихся не сдавших экзамен.
# отфильтровываем строки с баллом ниже значения столбца "Минимальный балл"
filtered_df = df[df['Балл'] < df['Минимальный балл']]

# вычисляем процент отфильтрованных строк
percentage = len(filtered_df) / len(df) * 100

print(f"Процент учащихся не сдавших экзамен: {percentage:.2f}%")

# 5 Постройте круговую диаграмму, показывающую распределение сдавших и не сдавших экзамен.
# отфильтровываем строки с баллом ниже значения столбца "Минимальный балл"
below_min_df = df[df['Балл'] < df['Минимальный балл']]

# отфильтровываем строки с баллом выше или равным значению столбца "Минимальный балл"
above_min_df = df[df['Балл'] >= df['Минимальный балл']]

# создаем список значений для круговой диаграммы
values = [len(below_min_df), len(above_min_df)]

# создаем список меток для круговой диаграммы
labels = ['Балл ниже Минимального балла', 'Балл выше или равен Минимальному баллу']

# строим круговую диаграмму
plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.show()

# 6 Постройте ядерную оценку плотности распределению баллов за экзамен.
sns.kdeplot(df['Балл'])
plt.show()

# 7 Найдите процентное соотношение учащихся, сдавших экзамен на «отлично», «хорошо», «удовлетворительно», «неудовлетворительно».
# находим значение первой строки столбца "Минимальный балл"
min_score = df.loc[0, 'Минимальный балл']

# отфильтровываем строки с баллом ниже значения первой строки столбца "Минимальный балл"
below_min_df = df[df['Балл'] < min_score]

# находим процентное соотношение строк с баллом ниже значения первой строки столбца "Минимальный балл"
below_min_percent = len(below_min_df) / len(df) * 100

# отфильтровываем строки с баллом от значения первой строки столбца "Минимальный балл" до 70
range1_df = df[(df['Балл'] >= min_score) & (df['Балл'] < 70)]

# находим процентное соотношение строк с баллом в диапазоне от значения первой строки столбца "Минимальный балл" до 70
range1_percent = len(range1_df) / len(df) * 100

# отфильтровываем строки с баллом от 71 до 90
range2_df = df[(df['Балл'] >= 71) & (df['Балл'] <= 90)]

# находим процентное соотношение строк с баллом в диапазоне от 71 до 90
range2_percent = len(range2_df) / len(df) * 100

# отфильтровываем строки с баллом от 91 до 100
range3_df = df[(df['Балл'] >= 91) & (df['Балл'] <= 100)]

# находим процентное соотношение строк с баллом в диапазоне от 91 до 100
range3_percent = len(range3_df) / len(df) * 100

# выводим результаты на экран
print(f"Балл ниже минимального балла: {below_min_percent:.2f}% (неудовлетворительно)")
print(f"Балл от {min_score} до 70: {range1_percent:.2f}% (удовлетворительно)")
print(f"Балл от 71 до 90: {range2_percent:.2f}% (хорошо)")
print(f"Балл от 91 до 100: {range3_percent:.2f}% (отлично)")

# 8 Какое процентное соотношение юношей и девушек писало данный экзамен?
counts = df['Пол'].value_counts()
percentages = counts / len(df) * 100
print(percentages)

# 9 Сколько школ принимало участие в экзамене?
num_schools = df['№ школы'].nunique()
print(f"{num_schools} школ принимало участие в экзамене")

# 10 Сколько всего заданий с кратким ответом? С развернутым ответом?
short_answer = df.at[0, 'Задания с кратким ответом']
length_short_answer = len(short_answer)
print(f"{length_short_answer} заданий с кратким ответом")

long_answer = df.at[0, 'Задания с развёрнутым ответом']
length_long_answer = len(re.sub(r'\([^()]*\)', '', long_answer))
print(f"{length_long_answer} заданий с развернутым ответом")

# 11 Пусть задания с кратким ответом будут задания типа В. Соответственно всего по экзамену вопросов класса В: В
# , ... Вк
#  Посчитайте процент выполненных и невыполненных заданий по каждому вопросу класса В.
_ = df["Задания с кратким ответом"]
print("№ задания: % невыполненных / % выполненных")
for i in range(length_short_answer):
    percentage = _.str[i].isin(['0', '-']).sum()/_.size
    print(f"Задание №{i}:",round(percentage*100, 2),"/",round(1 - percentage,2)*100)

# 12 Аналогично и с типом С (ответы с развернутым ответом)
_ = df["Задания с развёрнутым ответом"]
print("№ задания: % невыполненных / % выполненных")
for i in range(length_long_answer*4):
    if i%4==0:
        percentage = _.str[i].isin(['0']).sum()/_.size
        print(f"Задание №{i}: ",round(percentage*100, 2),"/",round(1 - percentage,2)*100)

# 13 Сделайте анализ по двум школам:
# по всем выполненным заданиям типа В
# по заданиям типа С больше 50%
# по среднему баллу юношей и девушек

A, B = 148, 152
score = df["Балл"][2:]
school_data = df["№ школы"][2:]
gender_data = df["Пол"][2:]

school_A_male_score = []
school_A_female_score = []

school_B_male_score = []
school_B_female_score = []

for i in range(2, len(score)):
    if school_data[i] == 148:
        if gender_data[i] == "М":
           school_A_male_score.append(score[i])
        if gender_data[i] == "Ж":
            school_A_female_score.append(score[i])
    if school_data[i] == 152:
        if gender_data[i] == "М":
            school_B_male_score.append(score[i])
        if gender_data[i] == "Ж":
            school_B_female_score.append(score[i])


print(np.mean(school_A_male_score))
print(np.mean(school_A_female_score))

print(np.mean(school_B_male_score))
print(np.mean(school_B_female_score))

