import json

import requests
from bs4 import BeautifulSoup


def main():
    domain = 'https://quotes.toscrape.com'
    start_url = '/'
    response = requests.get(f'{domain}{start_url}')
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = []
    authors = []
    tags = []

    while True:
        next_page = soup.find('li', class_='next')
        if not next_page:
            break
        next_page_url = next_page.find('a')['href']
        response = requests.get(f'{domain}{next_page_url}')
        soup = BeautifulSoup(response.text, 'lxml')

        quotes = quotes + soup.find_all('span', class_='text')
        authors = authors + soup.find_all('small', class_='author')
        tags = tags + soup.find_all('div', class_='tags')

    authors_collection = []
    quotes_collection = []

    for quote, author, tags in zip(quotes, authors, tags):

        author_info_link = author.find_next_sibling('a')['href']
        response = requests.get(f'{domain}{author_info_link}')
        soup = BeautifulSoup(response.text, 'lxml')
        author_born_date = soup.find('span', class_='author-born-date')
        author_born_location = soup.find('span', class_='author-born-location')
        author_description = soup.find('div', class_='author-description')
        tags = tags.find_all('a', class_='tag')

        tag_collection = []
        for tag in tags:
            tag_collection.append(tag.text)

        authors_collection.append({
            'fullname': author.text,
            'born_date': author_born_date.text,
            'born_location': author_born_location.text,
            'description': author_description.text.strip()
        })

        quotes_collection.append({
            "author": author.text,
            "quote": quote.text,
            "tags": tag_collection
        })

    with open('json/authors.json', 'w') as outfile:
        json.dump(authors_collection, outfile)

    with open('json/quotes.json', 'w') as outfile:
        json.dump(quotes_collection, outfile)

    print('Scraping Done!')


if __name__ == '__main__':
    main()
