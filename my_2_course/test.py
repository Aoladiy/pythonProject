# import numpy as np
# t = []
# for i in range(10000):
#     t.append(np.random.randint(0, 2))
# print(max(t))
# print(min(t))
import pandas as pd

file = pd.read_csv(r"C:\Users\Aldar\Downloads\id_tag_nsteps_0.csv", delimiter=';', on_bad_lines='skip')
print(file[:5])
