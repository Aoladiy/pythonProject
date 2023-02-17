import pandas as pd
from bs4 import BeautifulSoup

# 3.1
print("Задание 3.1")
dct = dict()
with open("../../data/steps_sample.xml") as file:
    recipes_xml = BeautifulSoup(file, "xml")
    counter = 0
    steps = [steps for steps in recipes_xml.recipes.find_all("steps")]
    for ident in recipes_xml.recipes.find_all("id"):
        ident = ident.contents[0]
        dct[ident] = [steps.contents[0] for steps in steps[counter].find_all("step")]
        counter += 1
    print(dct)

# 3.2
print("Задание 3.2")
with open("../../data/steps_sample.xml") as file:
    recipes_xml = BeautifulSoup(file, "xml")
    dct = {}
    steps = set()
    lst = []
    for length in recipes_xml.recipes.find_all("steps"):
        steps.add(len(length.find_all("step")))
    steps = sorted(steps)
    for check in recipes_xml.recipes.find_all("recipe"):
        check_ident = check.id.contents[0]
        check_length = len(check.steps.find_all("step"))
        lst.append((check_ident, check_length))
    for i in steps:
        t = []
        for j in lst:
            if i in j:
                t.append(j[0])
        dct[i] = t
    print(dct)

# 3.3
print("Задание 3.3")
with open("../../data/steps_sample.xml") as file:
    recipes_xml = BeautifulSoup(file, "xml")
    result_lst = []
    for i in recipes_xml.recipes.find_all("recipe"):
        ident = i.id.contents[0]
        steps = i.find_all("step")
        if "has_minutes" in str(steps) or "has_hours" in str(steps):
            result_lst.append(ident)
    print(result_lst)

# 3.4
print("Задание 3.4")
idents = []
steps = []
csv_file = pd.read_csv("../../data/recipes_sample.csv")
xml_file = BeautifulSoup(open("../../data/steps_sample.xml"), "xml")
for check in xml_file.find_all("recipe"):
    idents.append(int(*check.find("id")))
    steps.append(len(check.find_all("step")))
t = pd.DataFrame({"id": idents, "n": steps})
csv_file.loc[csv_file.n_steps.isna(), "n_steps"] = t.n
#print(csv_file.n_steps.head(20))

# 3.5
print("Задание 3.5")
if sum(csv_file.n_steps.isna()) == 0:
    print("нет пропусков")
    csv_file.n_steps.to_csv("recipes_sample_with_filled_nsteps.csv")