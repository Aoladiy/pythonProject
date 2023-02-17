import math

# Очиров Алдар ПИ21-7 лабораторная работа ч2
# многоногое
t = 'прабабка'
H0 = math.log(len(set(t)), 2)
lst = sorted([t.count(i) / len(t) for i in set(t)])  # частоты букв
H1 = -sum([i * math.log(i, 2) for i in lst])  # энтропия текста
print(f"R1 = {round(1 - H1 / H0, 3)}")


# создаёт набор уникальных комбинаций букв
lst1 = []
for i in t:
    for j in t:
        lst1.append(i + j)
lst1 = sorted(set(lst1))

lst2 = [(t + t[0]).count(i) for i in lst1]  # Сколько раз встречается каждая пара
# for i in lst1:
#     print(f"{i}, {t.count(i)}")  # код, чтобы проверить какая конкретная комбинация сколько раз встречается
#     lst2.append(t.count(i))
lst2 = list(filter(lambda x: x != 0, lst2))  # удаляю не встретившиеся пары (нули)
lst2 = list(map(lambda x: x / sum(lst2), lst2))  # нахожу частоты пар
Hxy = -sum([lst2.count(i) * (i * math.log(i, 2)) for i in set(lst2)])  # нахожу энтропия двухбуквенного текста
H2 = Hxy / 2  # энтропия на букву при учете двухбуквенных сочетаний
print(f"R2 = {round(1 - H2 / H0, 3)}")
