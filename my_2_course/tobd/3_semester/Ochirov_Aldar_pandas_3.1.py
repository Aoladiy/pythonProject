import json
import pandas as pd
import pickle
import os

# 1.1
print("Задача 1.1")
with open('../../data/contributors_sample.json', mode='r', encoding='utf-8') as file:
    file = json.load(file)
    print(list(map(lambda x: print(x), file[:3])))
print()

# 1.2
print("Задача 1.2")
result = set()
for i in range(len(file)):
    result.add(file[i]['address'])
print(result)
print()

# 1.3
print("Задача 1.3")


def function(username):
    with open('../../data/contributors_sample.json', mode='r', encoding='utf-8') as file:
        file = json.load(file)
        for i in range(len(file)):
            if username == file[i]['username']:
                return file[i]
            else:
                return ValueError


print(function('uhebert1'))
print()

# 1.4
print("Задача 1.4")
with open('../../data/contributors_sample.json', mode='r', encoding='utf-8') as file:
    file = json.load(file)
    male = 0
    female = 0
    for i in range(len(file)):
        if file[i]['sex'] == 'F':
            female += 1
        elif file[i]['sex'] == 'M':
            male += 1
    print(f'Мужчин - {male}', f'Женщин - {female}', sep='\n')
print()

# 1.5
print("Задача 1.5")
contributors = pd.read_json('../../data/contributors_sample.json')
contributors = contributors.iloc[:, [0, 2, 6]]
print(contributors)
print()

# 1.6
print("Задача 1.6")
recipes = pd.read_csv('../../data/recipes_sample.csv')
task_1_6 = pd.merge(contributors, recipes, left_on="id", right_on="contributor_id", how="right")
print(task_1_6.loc[task_1_6.username.isnull()])
print()

# 2.1
print("Задача 2.1")
contributors = pd.read_json('../../data/contributors_sample.json')
st = set()
for i in range(len(contributors)):
    t = contributors['jobs'][i]
    for i in t:
        st.add(i)

lst = list(st)
dct = {}
for i in range(len(lst)):
    lst1 = []
    for j in range(len(contributors)):
        if lst[i] in contributors["jobs"][j]:
            lst1.append(contributors["username"][j])
    dct[lst[i]] = lst1

print(dct)
print()

# 2.2
print("Задача 2.1")
pickle.dump(dct, open('../../data/job_people.pickle', 'wb'))
json.dump(dct, open('../../data/job_people.json', 'w'), indent=3)
print("pickle file", os.stat('../../data/job_people.pickle').st_size, "> then json file", os.stat(
    '../../data/job_people.json').st_size,
      "Done")
print()

# 2.3
print("Задача 2.3")
pl = pickle.load(open('../../data/job_people.pickle', 'rb'))
print(pl)
print()
