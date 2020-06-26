#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

base_url = 'https://gorod.dp.ua'
movies_url = base_url + '/afisha/tema/type/1'
patterns = ['Для всей семьи',
            'Мультфильм',
            'Фэнтези']


def get_movies():
    page = requests.get(movies_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    divs = soup.find_all('div', attrs={'style': 'padding:.5rem;max-width:30em;'})
    movies = {}
    for div in divs:
        result = 0
        text = str(div.text.encode('utf-8')).rstrip().lstrip()
        for pattern in patterns:
            result = text.find(pattern)
            result += result
            if result >= 0:
                movies[text.split('\n')[0]] = base_url + div.find('a')['href']
    return movies
