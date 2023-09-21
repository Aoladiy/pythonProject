import csv

import requests
from bs4 import BeautifulSoup


# Функция для загрузки HTML-страницы
def get_html(url):
    response = requests.get(url)
    return response.text


# Функция для парсинга отзывов
def parse_opinions(html):
    soup = BeautifulSoup(html, 'html.parser')
    opinions = []

    # Находим блок с отзывами
    opinions_block = soup.find('div', class_='review-list-wrap')
    if opinions_block:
        # Итерируемся по отзывам
        for opinion in opinions_block.find_all('div', class_='review-wrap'):
            restaurant_name_elem = opinion.find('div', class_='place-name-wrap').find('a')
            restaurant_name = restaurant_name_elem.text.strip() if restaurant_name_elem else "Не указано"

            user_name_elem = opinion.find('div', class_='user-name')
            user_name = user_name_elem.text.strip() if user_name_elem else "Анонимный пользователь"

            review_date_elem = opinion.find('div', class_='review-date')
            review_date = review_date_elem.text.strip() if review_date_elem else "Дата не указана"

            rating_value_elem = opinion.find('div', class_='review-rating').find('span')
            rating_value = rating_value_elem.text.strip() if rating_value_elem else "Оценка не указана"

            review_text_elem = opinion.find('span', class_='review-text-preview')
            review_text = review_text_elem.text.strip() if review_text_elem else "Отзыв не найден"

            # Дополнительно извлекаем информацию о категориях
            categories = {}
            rating_categories = opinion.find_all('div', class_='rating-category-name')
            rating_values = opinion.find_all('div', class_='rating-category-value')
            for cat_name, cat_value in zip(rating_categories, rating_values):
                cat_name = cat_name.text.strip()
                cat_value = int(cat_value.find('div', class_='rating-category-line')['style'].split(':')[1].strip('%;'))
                categories[cat_name] = cat_value

            # Добавляем информацию об отзыве в список
            opinions.append({
                'restaurant_name': restaurant_name,
                'user_name': user_name,
                'review_date': review_date,
                'rating_value': rating_value,
                'review_text': review_text,
                'categories': categories
            })

    return opinions


# Функция для получения списка страниц с отзывами
def get_all_review_pages(base_url):
    # Убираем слеш в конце базового URL, если он есть
    base_url = base_url.rstrip('/')
    pages = [base_url]
    html = get_html(base_url)
    base_url = base_url.split("/msk/opinions")[0]
    soup = BeautifulSoup(html, 'html.parser')

    # Находим элементы с номерами страниц
    page_numbers = soup.find('div', class_='pagination-wrapper').find_all('a', href=True)

    for page in page_numbers:
        page_url = page['href']
        if page_url and not page_url.startswith('javascript:'):
            full_page_url = base_url + page_url
            if full_page_url not in pages:
                pages.append(full_page_url)

    return pages


# Функция для сохранения данных в CSV-файл
def save_to_csv(opinions):
    all_categories = set()

    for opinion in opinions:
        i = list(map(lambda i: i[:-1], opinion['categories'].keys()))
        all_categories.update(i)

    with open('data/opinions.csv', mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['Ресторан', 'Пользователь', 'Дата отзыва', 'Общая оценка'] + list(all_categories) + [
            'Текст отзыва']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for opinion in opinions:
            # Создаем словарь с пустыми значениями для всех категорий
            row = {category: '' for category in all_categories}

            # Заполняем значениями из текущего отзыва
            row.update({
                'Ресторан': opinion['restaurant_name'],
                'Пользователь': opinion['user_name'],
                'Дата отзыва': opinion['review_date'],
                'Общая оценка': opinion['rating_value'],
                'Текст отзыва': opinion['review_text']
            })

            # Обновляем значения категорий оценок
            categories = {}
            for key in opinion['categories'].keys():
                categories[key[:-1]] = key[-1]
            row.update(categories)

            writer.writerow(row)


# Основная функция для запуска парсера
def main():
    base_url = 'https://www.restoran.ru/msk/opinions/'
    idx = 0
    all_review_pages = get_all_review_pages(base_url)
    all_opinions = []

    for page_url in all_review_pages:
        html = get_html(page_url)
        opinions = parse_opinions(html)
        all_opinions.extend(opinions)

    save_to_csv(all_opinions)
    print("Результаты сохранены в opinions.csv")


if __name__ == '__main__':
    main()
