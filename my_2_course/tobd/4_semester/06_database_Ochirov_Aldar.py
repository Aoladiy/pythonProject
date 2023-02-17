import sqlite3

# 1
import pandas as pd

con = sqlite3.connect("../../data/recipes.db")
cur = con.cursor()

# 2
sql_2 = """
create table Recipe (
    id integer primary key autoincrement not null,
    name varchar(255),
    minutes integer,
    submitted timestamp,
    description text,
    n_ingredients integer
)
"""
try:
    cur.execute(sql_2)
    con.commit()
except sqlite3.OperationalError as err:
    print("Ошибка:", err)

# 3
sql_3 = """
create table Review (
    id integer primary key autoincrement not null,
    user_id integer not null,
    recipe_id integer,
    date timestamp,
    rating integer,
    review text,
    foreign key (recipe_id) references 
    Recipe (id)
)
"""
try:
    cur.execute(sql_3)
    con.commit()
except sqlite3.OperationalError as err:
    print("Ошибка:", err)

# 4
# recipes_sample_with_tags_ingredients = recipes.merge(tags, left_on="id", right_on="id")
# recipes_sample_with_tags_ingredients.to_csv("../../data/recipes_sample_with_tags_ingredients")
reviews = pd.read_csv("../../data/reviews_sample.csv")
reviews.rename(columns={"Unnamed: 0": "id"}, inplace=True)

recipes = pd.read_csv("../../data/recipes_sample.csv")
recipes_sample = recipes[["id", "name", "minutes", "submitted", "description", "n_ingredients"]]

try:
    reviews.to_sql("Review", con, if_exists="append", index=False)
except sqlite3.IntegrityError as err:
    print("Ошибка:", err)

try:
    recipes_sample.to_sql("Recipe", con, if_exists="append", index=False)
except sqlite3.IntegrityError as err:
    print("Ошибка:", err)

# 5
sql_5 = """
select name from Recipe
where n_ingredients = 10
"""
cur = con.cursor()
cur.execute(sql_5)
print(*cur.fetchmany(5), sep="\n")
print("-" * 30)

# 6
sql_6 = """
select name from Recipe
where minutes = (
    select max(minutes)
    from Recipe)
"""
cur = con.cursor()
cur.execute(sql_6)
print(*cur.fetchall(), sep="\n")
print("-" * 30)

# 7
sql_7 = """
select * from Recipe
where id = ?
"""
id = (int(input("Введите id >>> ")),)
cur = con.cursor()
cur.execute(sql_7, id)
result = cur.fetchone()
if result:
    print(result)
else:
    print("Не найдено")
print("-" * 30)

# 8
sql_8 = """
select count(id) from Review
where rating = 5
"""
cur = con.cursor()
cur.execute(sql_8)
print(*cur.fetchall(), sep="\n")
print("-" * 30)

# 9
sql_9 = """
select count(id) from Review
where rating < 4 and review is Null
"""
cur = con.cursor()
cur.execute(sql_9)
print(*cur.fetchall(), sep="\n")
print("-" * 30)

# 10
sql_10 = """
select count(Recipe.id) from Review join Recipe on Review.recipe_id=Recipe.id
where minutes >= 15 and submitted between '2010-01-01' and '2010-12-31'
"""
cur = con.cursor()
cur.execute(sql_10)
print(*cur.fetchall(), sep="\n")
print("-" * 30)

# 11
sql_11 = """
select Recipe.id,
        name,
        user_id,
        date,
        rating
from Review join Recipe on Review.recipe_id=Recipe.id
where n_ingredients > 3
order by Recipe.id
"""
cur = con.cursor()
cur.execute(sql_11)
print(*cur.fetchall()[:10], sep="\n")
print("-" * 30)