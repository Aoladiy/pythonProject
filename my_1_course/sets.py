import matplotlib
import matplotlib_venn as mplv
from matplotlib import pyplot as plt

matplotlib.use("TkAgg")
set1 = {"Бергамонт", 'Морской аккорд'}
set2 = {"Герань", "Розмарин", "Шалфей"}
set3 = {"Ландан", "Пачули"}
a = mplv.venn3((len(set1), len(set2), 0, len(set3),
                0, 0, len(set1) + len(set2), + len(set3)),
               set_labels=('Верхние ноты', 'Средние ноты', 'Базовые ноты'))
plt.show()
