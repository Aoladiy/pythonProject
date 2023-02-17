import re

import bs4
import nltk
import pandas as pd
from bs4 import BeautifulSoup

#
# # Task 6.1.1
# print("Задание 6.1.1")
#
# recipes = pd.read_csv("../data/recipes_sample.csv")
#
# id = recipes.id.sample(n=5).to_list()
# minutes = recipes.minutes.sample(n=5).to_list()
#
# wide = 0
# for i in range(max(len(id), len(minutes))):
#     t = max(len(str(id[i])), len(str(minutes[i])))
#     if wide < t:
#         wide = t
# wide += 3
#
# print(f"|{"id":^{wide}}|{"minutes":^{wide}}|")
# print("|" + "-"*(wide*2 + 1) + "|")
# for i in range(5):
#     print(f"|{id[i]: ^{wide}}|{minutes[i]: ^{wide}}|")
#
# # Task 6.1.2
# print("Задание 6.1.2")
#
#
# def show_info(recipe_id=-1, is_step=False):
#     result_str = ""
#     recipes = pd.read_csv("../data/recipes_sample.csv")
#     data = recipes[recipes["id"] == recipe_id]
#
#     if recipe_id != -1:
#         name = data["name"].item()
#         with open("../data/steps_sample.xml", "r") as fp:
#             steps = BeautifulSoup(fp, "xml")
#             for recipe in steps.find_all("recipe"):
#                 if recipe.find("id").text == str(recipe_id):
#                     steps_str = [step.text for step in recipe.find_all("step")]
#                     break
#
#     result_str += """ + name.title() + ""\n\n"
#
#     for index in range(len(steps_str)):
#         result_str += str(index + 1) + ". " + steps_str[index].capitalize() + "\n"
#
#     result_str += 10 * "-" + "\nАвтор: " + str(data["contributor_id"].item()) + "\nСреднее время приготовления: " + str(
#         data["minutes"].item()) + " минут"
#
#     if is_step:
#         return steps_str
#     else:
#         return result_str
#
#
# # print(show_info(170895))
#
# # Task 6.1.3
# print("задание 6.1.3")
# recipes = pd.read_csv("../data/recipes_sample.csv")
# data = show_info(25082, is_step=True)
# pattern = re.compile(r"([\d]+ (hour[s]*|minute[s]*))")
# print(pattern.findall("\n".join(data)))
#
#
# # Task 6.1.4
# print("Задание 6.1.4")
# pattern = re.compile(r"^this.*[,] ?but")
# data = pd.Series(recipes.description).dropna()
# after_pattern = data.str.match(pattern)
# print(data[after_pattern].sample(n=3))


# Task 6.2.1
print("Задание 6.2.1")
with open("../../data/steps_sample.xml") as file:
    recipes_xml = BeautifulSoup(file, "xml")
    lst = []
    pattern = re.compile(r"[0-9] / [0-9]")
    for i in recipes_xml.recipes.find_all("recipe"):
        if i.id.contents[0] == "72367":
            steps = i.find_all("step")
            for j in steps:
                lst.append(" ".join(j.contents))
            print("before:", lst)
            for z in range(len(lst)):
                t = re.findall(pattern, lst[z])
                if t:
                    t_without_spaces = t[0].replace(' ', '')
                    lst[z] = lst[z].replace(t[0], t_without_spaces)
            print("after:", lst)

# Task 6.2.2
print("Задание 6.2.2")
with open('../../data/steps_sample.xml') as file:
    recipes_xml = BeautifulSoup(file, 'xml')
    set_w = set()
    for i in recipes_xml.find_all('recipe'):
        set_w.update(nltk.word_tokenize(i.steps.text))
    set_wo = set_w.copy()
    for i in set_wo:
        if i.isalpha() == False:
            set_w.remove(i)
    print(len(set_w))


# Task 6.2.3
print("Задание 6.2.3")
with open('../../data/steps_sample.xml') as file:
    recipes = pd.read_csv('../../data/recipes_sample.csv')
    recipes_xml = BeautifulSoup(file, 'xml')
    recipes_d = recipes['description'].fillna("null").apply(nltk.sent_tokenize)
    [print("Length:", len(i), i) for i in sorted(recipes_d, key=lambda recipes_d: len(recipes_d), reverse=True)[:5]]


# Task 6.2.4
print("Задание 6.2.4")


def func_6_2_4(number_of_sentence):
    recipes = pd.read_csv('../../data/recipes_sample.csv')
    inform = nltk.pos_tag(nltk.word_tokenize(recipes[recipes['id'] == number_of_sentence].name.values[0]))
    print(''.join([f"{j:{len(i) + 1}}" for i, j in inform]) + '\n' + ''.join([f"{i:{len(i) + 1}}" for i, j in inform]))


func_6_2_4(241106)
