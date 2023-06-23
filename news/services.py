# news/services.py

import requests
from django.conf import settings


def get_news():
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': 'us',
        'apiKey': settings.NEWS_API_KEY,
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data['articles']

