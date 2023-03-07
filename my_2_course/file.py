import pandas as pd

# 1
# загружаем данные из Excel файла
df = pd.read_excel('имя_файла.xlsx')

# получаем описательную статистику для всех количественных столбцов
desc_stats = df.describe()
print(desc_stats)

# 2
# вычисляем среднее значение для столбца "Балл"
mean_score = df['Балл'].mean()

# отфильтровываем строки с баллом ниже среднего
filtered_df = df[df['Балл'] < mean_score]

# вычисляем процент отфильтрованных строк
percentage = len(filtered_df) / len(df) * 100

print("Процент строк с баллом ниже среднего:", percentage, "%")