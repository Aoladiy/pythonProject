import pandas as pd
recipes = pd.read_csv(r'C:\Users\Aldar\PycharmProjects\pythonProject\что я накалякал 2 курс\recipes_sample.csv')
reviews = pd.read_csv(r'C:\Users\Aldar\PycharmProjects\pythonProject\что я накалякал 2 курс\reviews_sample.csv')

# 3.1
print(recipes.columns)
recipes.insert(8, 'description_length', recipes['description'].str.len())
print(recipes.columns)
print()

# 3.2
recipes['name'] = recipes['name'].str.title()
print(recipes['name'])
print()

# 3.3
recipes.insert(9, 'name_word_count', recipes['name'].str.split().str.len())
print(recipes['name_word_count'])
print()

# 4.1
print('Задание 4.1', '\n')
print(recipes.groupby('contributor_id')['id'].count())
print()

# 4.2
print('Задание 4.2', '\n')
print(f"Средний рейтинг к каждому из рецептов\n{reviews.groupby('recipe_id')['rating'].mean()}")
print(f"Отсутствуют отзывы для {reviews['review'].isna().sum()} рецептов")
print()

# 4.3
print('Задание 4.3', '\n')
print(f"{recipes.groupby('submitted')['id'].count()}")
print()

# 5.1
print('Задание 5.1', '\n')
df5_1 = recipes.merge(reviews.dropna(how='any'), left_on='id', right_on='recipe_id').drop(['minutes', 'contributor_id', 'submitted', 'n_steps', 'description', 'n_ingredients', 'Unnamed: 0', 'date', 'review', 'recipe_id'], axis=1).reindex(columns=['id', 'name', 'user_id', 'rating'])
print(df5_1)
print()

# 6.1
print('Задание 6.1', '\n')
df6_1 = recipes.sort_values(by='name_word_count', ascending=False)
recipes.to_csv('6_1.csv')
print()

# 6.2
print('Задание 6.2', '\n')
with pd.ExcelWriter('../../data/6_2.xlsx') as file:
    df5_1.to_excel(file, sheet_name='Рецепты с оценками')
print()
