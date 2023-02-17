import xlwings as xw
import pandas as pd
import numpy as np
import csv
from matplotlib import pyplot as plt

# 1
reviews = pd.read_csv("../../data/reviews_sample.csv")
reviews.rename(columns={'Unnamed: 0': 'id'}, inplace=True)
recipes = pd.read_csv("../../data/recipes_sample.csv",
                      usecols=["id", "name", "minutes", "submitted", "description", "n_ingredients"])

# 2
wb = xw.Book('recipes.xlsx')
sht1 = wb.sheets.add("Отзывы")
sht = wb.sheets.add("Рецепты")
wb.sheets['Лист1'].delete()
sht.range('A1').value = recipes.sample(n=int(recipes.shape[0] * 0.05))
sht1.range('A1').value = reviews.sample(n=int(reviews.shape[0] * 0.05))

# 3
xw.Range('H1').value = 'seconds_assign'
xw.Range("H2").options(transpose=True).value = sht.range('D2:D1501').options(np.array).value * 60

# 4
xw.Range('I1').value = 'seconds_formula'
formula = xw.Range('I2').formula = f'=D2*60'
xw.Range("I2:I1501").formula = formula

# 5
sht.range('H1').api.HorizontalAlignment = xw.constants.HAlign.xlHAlignCenter
sht.range('I1').api.HorizontalAlignment = xw.constants.HAlign.xlHAlignCenter
sht.range('H1').api.Font.Bold = True
sht.range('I1').api.Font.Bold = True

# 6
for cell in sht["D2:D1501"]:
    if cell.value > 10:
        cell.color = (255, 0, 0)
    elif 5 <= cell.value <= 10:
        cell.color = (255, 223, 0)
    elif cell.value < 5:
        cell.color = (0, 214, 120)

# 7
sht.range('J1').value = 'n_reviews'
formula_for_7 = sht.range('J2').formula = f'=COUNTIF(Отзывы!$D$2:$D$6335,C2)'
sht.range('J2:J1501').value = formula_for_7

# 8
rating = sht1["F2:F6335"].value
recipe_id = sht1["D2:D6335"].value
id_res = sht["B2:B1501"].value


def validate():
    for i in range(len(rating)):
        if not (0 <= rating[i] <= 5) or (recipe_id[i] not in id_res):
            sht1[f"A{i + 2}:G{i + 2}"].color = (255, 0, 0)


validate()

# 9
wb_r_m = xw.Book("recipes_model.csv")
sht2 = wb_r_m.sheets.add(name="Модель")
wb_r_m.sheets[1].delete()

with open("../../data/recipes_model.csv", "r", encoding="utf-8") as file:
    df_for_9 = pd.DataFrame(csv.reader(file, delimiter='\t'))

sht2.range('A2').options(index=False, header=False).value = df_for_9

# 10
formula_for_10 = xw.Range(
    'J2').formula = f'=CONCAT(B2, " ", UPPER(C2), " ", IFS(G2="PK", "PRIMARY KEY", G2="FK",CONCAT("REFERENCES", " (", H2, " ", I2, ")" ),ISBLANK(G2),""), IF(AND(D2="Y",G2<>"PK"), " NOT NULL", ""))'
xw.Range(f"J2:J18").formula = formula_for_10

# 11
sht2["A1:J1"].color = "00ccff"
sht2.autofit(axis="columns")
sht2.range('A1:J1').api.Font.Bold = True
sht2.range('A1:J1').api.AutoFilter(Field := 1)

# 12
sht3 = wb_r_m.sheets.add(name="Статистика")
dct = {}

var = list(set([i for i in sht2["$A$2:$A$18"].value]))
sht3.range("A1:A3").options(transpose=True).value = list(var)

for i in range(1, len(var) + 1):
    xw.Range(f"B{i}").formula = f'=COUNTIF(МОДЕЛЬ!$A$2:$A$18, A{i})'
    dct[var[i - 1]] = [sht3[f"B{i}"].value]

df_for_12 = pd.DataFrame.from_dict(dct)

plot = df_for_12.plot(kind="bar")
plt.savefig(r'saved_figure.png')
sht3.pictures.add(image=r"C:\Users\Aldar\PycharmProjects\pythonProject\что я накалякал 2 курс\saved_figure.png", name='MyPlot',
                  left=sht3.range("E2").left, update=True)
