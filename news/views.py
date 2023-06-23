from django.shortcuts import render

# Create your views here.
# news/views.py

from django.shortcuts import render
from .services import get_news

def news_view(request):
    articles = get_news()
    return render(request, 'news.html', {'articles': articles})
