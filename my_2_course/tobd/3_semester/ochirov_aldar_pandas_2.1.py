import numpy as np
import pandas as pd

# 1.1
recipes = pd.read_csv('../../data/recipes_sample.csv')
reviews = pd.read_csv('../../data/reviews_sample.csv')
print()

# 1.2
print(f'(recipes) количество точек данных (строк) >>> {recipes.shape[0]}')
print(f'(recipes) количество столбцов >>> {recipes.shape[1]}')
print(f'(recipes) тип данных каждого столбца:\n{recipes.dtypes}')
print(f'(reviews) количество точек данных (строк) >>> {reviews.shape[0]}')
print(f'(reviews) количество столбцов >>> {recipes.shape[1]}')
print(f'(reviews) тип данных каждого столбца:\n{recipes.dtypes}')
print()

# 1.3
print(f'(recipes) строки с пропусками к строкам без {np.unique(np.where(pd.isnull(recipes))).size / (recipes.shape[0] - np.unique(np.where(pd.isnull(recipes))).size)}')
print(f'(reviews) строки с пропусками к строкам без {np.unique(np.where(pd.isnull(reviews))).size / (reviews.shape[0] - np.unique(np.where(pd.isnull(reviews))).size)}')
print()

# 1.4
print(f'(recipes) средние значения по столбцам: \n{recipes.mean(numeric_only=True)}')
print(f'(reviews) средние значения по столбцам: \n{reviews.mean(numeric_only=True)}')
print()

# 1.5
print(f'(recipes) 10 случайных имён: \n{recipes.name[np.random.randint(1, recipes.shape[0], 10)]}')
print()

# 1.6
# reviews.index += 1
print(reviews.index)

# 1.7
print(recipes.where(recipes.iloc[:, 7] <= 5).where(recipes.iloc[:, 2] <= 20).dropna())
print()

# 2.1
# print(recipes['submitted'])
recipes['submitted'] = pd.to_datetime(recipes['submitted'])
print(recipes['submitted'])
print()

# 2.2
print(recipes[recipes['submitted'] <= pd.to_datetime("2010-01-01")])
print()

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
