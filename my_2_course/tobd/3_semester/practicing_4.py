import xlwings as xw
book = xw.Book("себестоимостьА_в1.xlsx")
sht = book.sheets("Рецептура")
def func(amount, prices, result_place):
    prices = list(sht.range(prices).value)
    for i in range(len(prices)):
        if prices[i] is None:
            prices[i] = 0
    vengerskiy = list(sht.range(amount).value)
    for i in range(len(vengerskiy)):
        if vengerskiy[i] is None:
            vengerskiy[i] = 0
    vengerskiy_result = sum(map(lambda x: x[0] * x[1], zip(vengerskiy, prices)))
    sht.range(result_place).value = vengerskiy_result
    print("себестоимость венгерсокго хлеба >>>", vengerskiy_result)

func("G14:O14", "G7:O7", "R7")
func("G13:O13", "G7:O7", "R6")
func("G12:O12", "G7:O7", "R5")
func("G11:O11", "G7:O7", "R4")