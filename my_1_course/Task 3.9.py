from matplotlib import pyplot as plt
from matplotlib_venn import venn3
videocards = (
    'rtx 3090', 'rtx 3080 ti', 'rtx 3080', 'rtx 3070 ti', 'rtx 3070', 'rtx 3060 ti', 'rtx 3060', 'rtx 2080s',
    'rtx 2080', 'rtx 2070s', 'rtx 2070', 'rtx 2060s', 'rtx 2060', 'gtx 1660 ti', 'gtx 1660s', 'gtx 1660', 'gtx 1650 ti',
    'gtx 1650', 'gtx 1080 ti', 'gtx 1080', 'gtx 1070 ti', 'gtx 1070', 'gtx 1060', 'gtx 1050 ti', 'gtx 1050')
processors = (
    'i9 9980xe', 'i9 9900kf', 'i7 6900k', 'i7 7700k', 'i5 12600k', 'i5 9400f', 'i3 9350kf', 'i3 10105f',
    'Pentium g5400', 'Celeron g1840', 'ryzen 9 5950x', 'ryzen 9 3900', 'ryzen 7 5800x', 'ryzen 7 1700', 'ryzen 5 5600x',
    'ryzen 5 1500x', 'ryzen 3 4300ge', 'ryzen 3 1200')
RAM = ('2x32 3600', '4x16 3000', '2x16 4800', '4x8 3000', '2x8 3600', '8 2666', '2x4 2666', '4 2666')
venn3(subsets=(16, 16, 0, 8, 0, 0, 15), set_labels=('Видеокарты 64%', 'Процессоры 88%', 'ОЗУ 100%'))
plt.title('Комплектующие')
plt.show()
