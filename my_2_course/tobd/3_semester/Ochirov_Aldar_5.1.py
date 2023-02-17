import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
import seaborn as sns

# # 5.1, Task 1
# print("Задача 1")
# data1_1 = np.load("../data/average_ratings.npy")
# fig1_1 = plt.figure()  # creating picture
#
# x = np.linspace(0, len(data1_1[0]), len(data1_1[0]))  # creating axis x
# line1_1 = data1_1[0]  # reading waffle iron french toast
# line1_2 = data1_1[1]  # reading zwetschgenkuchen bavarian plum cake
# line1_3 = data1_1[2]  # reading lime tea
#
# ax1_1 = fig1_1.add_axes([0.1, 0.1, 0.85, 0.8])  # adding coordinate system
#
# # adding charts
# ax1_1.plot(x, line1_1, "y")
# ax1_1.plot(x, line1_2, "g")
# ax1_1.plot(x, line1_3, "r")
#
# # adding beautiful features
# ax1_1.set_xlabel("Номер дня")
# ax1_1.set_ylabel("Средний рейтинг")
# ax1_1.set_title("Изменение среднего рейтинга трех рецептов")
# ax1_1.legend(["waffle iron french toast", "zwetschgenkuchen bavarian plum cake", "lime tea"], loc="upper left")
#
# fig1_1.show()
#
# # 5.1, Task 2
# print("Задача 2")
# fig2_1 = plt.figure()
#
# freq = pd.date_range(start="01.01.2019", end="30.12.2021")
# ax2_1 = fig2_1.add_axes([0.1, 0.1, 0.85, 0.8])
#
# ax2_1.plot(freq, line1_1, "y")
# ax2_1.plot(freq, line1_2, "g")
# ax2_1.plot(freq, line1_3, "r")
#
# ax2_1.legend(["waffle iron french toast", "zwetschgenkuchen bavarian plum cake", "lime tea"], loc="upper left")
# ax2_1.set_xlabel("Дата")
# ax2_1.set_ylabel("Средний рейтинг")
# ax2_1.set_title("Изменение среднего рейтинга трех рецептов")
#
# ax2_1.xaxis.set_minor_locator(mdates.MonthLocator())
# ax2_1.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 13)))
# fig2_1.show()
#
# # 5.1, Task 3
# print("Задача 3")
# fig3_1, ax3_1 = plt.subplots(3, 1, figsize=(6.4, 7), constrained_layout=True)
#
# freq = pd.date_range(start="01.01.2019", end="30.12.2021")
#
# ax3_1[0].plot(freq, line1_1, "y")
# ax3_1[1].plot(freq, line1_2, "g")
# ax3_1[2].plot(freq, line1_3, "r")
#
# ax3_1[0].set_title("waffle iron french toast", loc="left", y=0.85, x=0.02, fontsize="medium")
# ax3_1[0].set_ylabel("Средний рейтинг")
# ax3_1[0].set_xticklabels([])
# ax3_1[1].set_title("zwetschgenkuchen bavarian plum cake", loc="left", y=0.85, x=0.02, fontsize="medium")
# ax3_1[1].set_ylabel("Средний рейтинг")
# ax3_1[1].set_xticklabels([])
# ax3_1[2].set_title("lime tea", loc="left", y=0.85, x=0.02, fontsize="medium")
# ax3_1[2].set_ylabel("Средний рейтинг")
#
# ax3_1[0].xaxis.set_minor_locator(mdates.MonthLocator())
# ax3_1[0].xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 13)))
# ax3_1[1].xaxis.set_minor_locator(mdates.MonthLocator())
# ax3_1[1].xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 13)))
# ax3_1[2].xaxis.set_minor_locator(mdates.MonthLocator())
# ax3_1[2].xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 13)))
# fig3_1.show()
#
# # 5.1, Task 4
# print("Задание 4")
# data = np.load("../data/visitors.npy")
#
# fig4_1, ax4_1 = plt.subplots(1, 2, figsize=(12, 3), constrained_layout=True)
# fig4_1.suptitle("Изменение количества пользователей в линейном и логарифмическом масштабе", y=1.2, fontsize=20)
#
# ax4_1[0].plot(range(100), data, "g")
# ax4_1[0].plot(range(100), [100] * 100, "r")
# ax4_1[0].set_xlabel("Количество дней с момента акции")
# ax4_1[0].set_ylabel("Число посетителей")
# ax4_1[0].set_title("$y(x)=\lambda e^{-\lambda x}$")
# ax4_1[0].annotate("$y(x)=100$", xy=(50, 200))
#
# ax4_1[1].plot(range(100), data, "g")
# ax4_1[1].plot(range(100), [100] * 100, "r")
# ax4_1[1].set_yscale("log")
# ax4_1[1].set_xlabel("Количество дней с момента акции")
# ax4_1[1].set_ylabel("Число посетителей")
# ax4_1[1].set_title("$y(x)=\lambda e^{-\lambda x}$")
# ax4_1[1].annotate("$y(x)=100$", xy=(40, 120))
#
# fig4_1.show()


# 5.2, Task 5
print("Задание 5")
recipes = pd.read_csv("../../data/recipes_sample.csv")
reviews = pd.read_csv("../../data/reviews_sample.csv")

short = recipes[recipes["minutes"] < 5]
medium = recipes[(recipes["minutes"] >= 5) & (recipes["minutes"] < 50)]
long = recipes[recipes["minutes"] >= 50]

short_mean = short["n_steps"].mean()
medium_mean = medium["n_steps"].mean()
long_mean = long["n_steps"].mean()

result_df_5_1 = pd.DataFrame({"Recipes group": ["short", "medium", "long"], "Length": [short_mean, medium_mean, long_mean]})

result_df_5_1.plot(kind="bar", x="Recipes group", y="Length", ylabel="average number of steps")
plt.show()

result_df_5_1.Length.value_counts().plot(kind="pie", ylabel="Recipe groups")
plt.show()


# 5.2, Task 6
print("Задание 6")
reviews["date"] = pd.to_datetime(reviews["date"])
reviews8 = reviews[(reviews["date"] >= pd.to_datetime("2008-1-1")) & (reviews["date"] <= pd.to_datetime("2008-12-31"))]
reviews9 = reviews[(reviews["date"] >= pd.to_datetime("2009-1-1")) & (reviews["date"] <= pd.to_datetime("2009-12-31"))]
reviews8 = reviews8["rating"]
reviews9 = reviews9["rating"]

# print(len(reviews8["date"]))
# print(len(reviews9["date"]))
# print(len(reviews8["date"]) + len(reviews9["date"]))
fig6_1 = plt.figure(figsize=(12, 6), constrained_layout=True)

ax6_1 = fig6_1.add_subplot(1, 3, 1)
ax6_1.set_xlabel("2008 year")
reviews8.plot(ax=ax6_1, kind='hist')

ax6_2 = fig6_1.add_subplot(1, 3, 2)
ax6_2.set_xlabel("2009 year")
reviews9.plot(ax=ax6_2, kind='hist')
fig6_1.show()


# 5.2, Task 7
print("Задание 7")
recipes7_1 = recipes.copy()

recipes7_1.loc[recipes7_1.minutes >= 50, "type"] = "long"
recipes7_1.loc[(recipes7_1.minutes > 5) & (recipes7_1.minutes < 50), "type"] = "medium"
recipes7_1.loc[recipes7_1.minutes <= 5, "type"] = "low"

sns.displot(recipes7_1, x="n_steps", y="n_ingredients", hue="type")
plt.title('Диаграмма рассеяния n_steps и n_ingredients')
plt.show()